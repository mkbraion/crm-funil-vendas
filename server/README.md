# Baixador de vídeos (backend)

Serviço em Flask + [yt-dlp](https://github.com/yt-dlp/yt-dlp) que baixa vídeos
de **Medal, TikTok, Pinterest e Instagram**. É separado do CRM: o navegador
sozinho não consegue baixar desses sites (CORS + download forçado), então o
yt-dlp roda aqui no servidor.

**Sem API paga e sem teto de requisição.** O único custo é a banda/hospedagem
de onde isso roda.

## Endpoints

| Método | Rota            | O que faz                                        |
|--------|-----------------|--------------------------------------------------|
| GET    | `/`             | Healthcheck                                       |
| GET    | `/api/info?url=`| Título, thumbnail e duração (para pré-visualizar) |
| POST   | `/api/download` | Baixa e devolve o arquivo (`{ "url": "..." }`)    |

## Rodar local

```bash
cd server
pip install -r requirements.txt
python app.py           # sobe em http://localhost:5000
```

Precisa do **ffmpeg** instalado (o Docker já inclui). No Ubuntu: `sudo apt install ffmpeg`.

Teste rápido:

```bash
curl -X POST http://localhost:5000/api/download \
  -H "Content-Type: application/json" \
  -d '{"url":"https://medal.tv/..."}' -o video.mp4
```

## Deploy no Render

Este diretório tem um `render.yaml`. No painel do Render: **New → Blueprint**,
aponte para este repositório e ele sobe o serviço `crm-downloader` sozinho.
Depois é só colar a URL pública (ex.: `https://crm-downloader.onrender.com`)
no campo **Servidor** da página `baixador.html`.

> No plano **free** do Render a instância dorme após 15 min de inatividade
> (o primeiro acesso demora ~30–50s) e a banda é limitada (~100 GB/mês).
> Vídeo é pesado; se o uso crescer, suba para o plano `starter`.

## Variáveis de ambiente

| Variável          | Padrão | O que é                                       |
|-------------------|--------|-----------------------------------------------|
| `MAX_FILESIZE_MB` | `300`  | Tamanho máximo por download (limite técnico)  |
| `SOCKET_TIMEOUT`  | `30`   | Timeout de rede do yt-dlp (segundos)          |
| `PORT`            | `8000` | Porta (o Render define automaticamente)       |

## Aviso legal

Baixar de TikTok/Pinterest/Instagram pode ferir os Termos de Serviço dessas
plataformas. Use para conteúdo próprio ou com permissão. Baixar mídia com
direitos autorais sem autorização é responsabilidade de quem usa.
