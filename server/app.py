"""
Baixador de vídeos (Medal, TikTok, Pinterest e Instagram) via yt-dlp.

É um serviço à parte do CRM — roda o yt-dlp no servidor porque o navegador
sozinho não consegue baixar desses sites (CORS + download forçado). Sem API
paga e sem teto de requisição: o único custo real é a banda/hospedagem.

Endpoints:
  GET  /                -> healthcheck
  GET  /api/info?url=   -> metadados (título, thumb, duração) p/ pré-visualizar
  POST /api/download    -> baixa e devolve o arquivo como anexo
"""

import os
import shutil
import tempfile
from pathlib import Path
from urllib.parse import urlparse

from flask import Flask, request, jsonify, send_file, after_this_request
from flask_cors import CORS
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

app = Flask(__name__)
CORS(app)  # libera chamadas do frontend (GitHub Pages)

# Domínios liberados — impede que o serviço vire um proxy aberto (SSRF).
ALLOWED_BASE_HOSTS = (
    "medal.tv",
    "tiktok.com",
    "pinterest.com",
    "pin.it",
    "instagram.com",
    "instagr.am",
)

# Tetos de segurança (não de cobrança) — ajustáveis por variável de ambiente.
MAX_FILESIZE = int(os.environ.get("MAX_FILESIZE_MB", "300")) * 1024 * 1024
SOCKET_TIMEOUT = int(os.environ.get("SOCKET_TIMEOUT", "30"))


def host_allowed(url: str) -> bool:
    """True se a URL for http(s) e o domínio estiver na lista liberada."""
    try:
        parsed = urlparse(url)
    except Exception:
        return False
    if parsed.scheme not in ("http", "https"):
        return False
    host = (parsed.netloc or "").lower().split(":")[0]
    if not host:
        return False
    return any(host == base or host.endswith("." + base) for base in ALLOWED_BASE_HOSTS)


def platform_of(url: str) -> str:
    host = (urlparse(url).netloc or "").lower()
    if "medal.tv" in host:
        return "Medal"
    if "tiktok" in host:
        return "TikTok"
    if "pinterest" in host or "pin.it" in host:
        return "Pinterest"
    if "instagr" in host:
        return "Instagram"
    return "vídeo"


def base_opts() -> dict:
    return {
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "socket_timeout": SOCKET_TIMEOUT,
        "retries": 2,
        # User-agent de navegador ajuda em alguns sites (ex.: Pinterest/Instagram).
        "http_headers": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/122.0 Safari/537.36"
            )
        },
    }


def _read_url() -> str:
    if request.is_json:
        return ((request.get_json(silent=True) or {}).get("url") or "").strip()
    return (request.form.get("url") or "").strip()


@app.get("/")
def health():
    return jsonify(ok=True, service="baixador", platforms=list(ALLOWED_BASE_HOSTS))


@app.get("/api/info")
def info():
    url = (request.args.get("url") or "").strip()
    if not url:
        return jsonify(error="Informe uma URL."), 400
    if not host_allowed(url):
        return jsonify(error="Domínio não suportado. Use Medal, TikTok, Pinterest ou Instagram."), 400
    try:
        with YoutubeDL({**base_opts(), "skip_download": True}) as ydl:
            data = ydl.extract_info(url, download=False)
    except DownloadError:
        return jsonify(error="Não consegui ler esse link. Pode ser privado, ter expirado ou exigir login."), 422
    except Exception:
        return jsonify(error="Erro ao processar o link."), 500

    # Alguns extratores devolvem uma lista de entradas — pega a primeira.
    if data.get("_type") == "playlist" and data.get("entries"):
        data = data["entries"][0]

    return jsonify(
        platform=platform_of(url),
        title=data.get("title") or "vídeo",
        thumbnail=data.get("thumbnail"),
        duration=data.get("duration"),
        uploader=data.get("uploader") or data.get("uploader_id"),
    )


@app.post("/api/download")
def download():
    url = _read_url()
    if not url:
        return jsonify(error="Informe uma URL."), 400
    if not host_allowed(url):
        return jsonify(error="Domínio não suportado. Use Medal, TikTok, Pinterest ou Instagram."), 400

    tmpdir = tempfile.mkdtemp(prefix="dl_")
    opts = {
        **base_opts(),
        "outtmpl": os.path.join(tmpdir, "%(title).80s.%(ext)s"),
        # Prioriza um único arquivo mp4 (não exige ffmpeg); cai pro melhor disponível.
        "format": "best[ext=mp4]/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best",
        "merge_output_format": "mp4",
        "max_filesize": MAX_FILESIZE,
    }

    try:
        with YoutubeDL(opts) as ydl:
            ydl.extract_info(url, download=True)
    except DownloadError:
        shutil.rmtree(tmpdir, ignore_errors=True)
        return jsonify(error="Não consegui baixar esse link. Pode ser privado, ter expirado ou exigir login."), 422
    except Exception:
        shutil.rmtree(tmpdir, ignore_errors=True)
        return jsonify(error="Erro inesperado ao baixar."), 500

    files = [p for p in Path(tmpdir).iterdir() if p.is_file()]
    if not files:
        shutil.rmtree(tmpdir, ignore_errors=True)
        return jsonify(error="Nada foi baixado. O vídeo pode ter passado do tamanho máximo permitido."), 422

    # Maior arquivo = o vídeo final (descarta thumbs/fragmentos residuais).
    final = max(files, key=lambda p: p.stat().st_size)

    @after_this_request
    def cleanup(response):
        shutil.rmtree(tmpdir, ignore_errors=True)
        return response

    return send_file(final, as_attachment=True, download_name=final.name)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
