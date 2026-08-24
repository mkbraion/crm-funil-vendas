# Merseu Store 🛍️💚

Site de e-commerce de moda streetwear (mesmo tema/estrutura de uma loja como a Flóretom), com identidade visual da **Merseu Store** em **verde e preto**.

## O que tem

- **Página única, responsiva e sem dependências** (`index.html`) — HTML/CSS/JS puro, funciona abrindo direto no navegador.
- **Barra de avisos** (frete fixo, rastreio via WhatsApp, PIX com desconto).
- **Header fixo** com logo, menu, busca, carrinho e menu mobile.
- **Hero** com chamada, CTAs e selos de confiança.
- **Categorias** clicáveis (Camisas, Tênis, Acessórios, Perfumes, Shorts, Relógios).
- **Grade de produtos** com filtro por categoria, preços, descontos e avaliações.
- **Carrinho lateral (drawer)** funcional com quantidades e persistência em `localStorage`.
- **Checkout via WhatsApp**: monta a mensagem do pedido e abre o `wa.me`.
- **Botão flutuante do WhatsApp**, newsletter, seção "Quem Somos" e rodapé completo.

## Personalização rápida

- **Número de WhatsApp**: edite a constante `WHATSAPP` no início do `<script>` (formato `55DDDNÚMERO`).
- **Produtos**: edite o array `PRODUCTS`. Para fotos reais, troque o `emoji` por uma `<img>` no card (função `renderGrid`).
- **Cores**: ajuste as variáveis em `:root` (`--green`, `--bg`, etc.).

## Como abrir

Abra `merseu-store/index.html` no navegador — não precisa de build nem servidor.
