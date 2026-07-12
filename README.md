# CRM · Funil de Vendas

Um CRM enxuto que roda no navegador. Abre e usa: cadastra o lead, move pelo funil e acompanha a conversão na hora. Por padrão os dados ficam salvos no próprio navegador — e, se você quiser, dá pra **criar uma conta e sincronizar na nuvem** para acessar os leads de qualquer aparelho.

**No ar:** https://mkbraion.github.io/crm-funil-vendas/

## O que dá pra fazer

Cadastrar leads (nome, WhatsApp, valor, origem e observação), mover entre as etapas — Novo → Em contato → Proposta → Ganho —, marcar como perdido, chamar no WhatsApp direto do card e exportar tudo em JSON.

No topo ficam os quatro números que interessam: leads ativos, valor no funil, valor ganho e taxa de conversão. Tudo recalcula sozinho conforme você mexe.

## Rodar

Abre o `index.html`. É isso. Pra acessar de qualquer lugar, joga no GitHub Pages (os dados ficam por navegador/aparelho).

## Sincronização na nuvem (multi-dispositivo)

Clique em **"☁️ Entrar na nuvem"**, crie uma conta e pronto: os leads passam a ser salvos no backend [crm-api](https://github.com/mkbraion/crm-api) e ficam disponíveis em qualquer navegador/celular. Sem login, tudo continua funcionando localmente.

- Cada conta só enxerga os próprios leads (isolamento por usuário).
- Na primeira vez, ele oferece **subir os leads locais** para a nuvem.
- Se o servidor cair ou a sessão expirar, volta ao modo local sem perder nada.

O endereço do servidor pode ser ajustado no próprio login (campo "Servidor"), caso você hospede o [crm-api](https://github.com/mkbraion/crm-api) em outra URL.

## Próximos passos

Lembrete de follow-up pra não esquecer de retornar o cliente, e arrastar-e-soltar entre as colunas.
