<!-- MKBRAION-POLISH:START -->
<div align="center">

# CRM Funil Vendas

**CRM de funil de vendas com interface Kanban, funcionamento offline, armazenamento local e sincronização com API própria.**

[![Repositório](https://img.shields.io/badge/GitHub-Repositório-181717?logo=github)](https://github.com/mkbraion/crm-funil-vendas) [![Demo ao vivo](https://img.shields.io/badge/Demo-Abrir%20aplicação-2ea44f?logo=vercel)](https://mkbraion.github.io/crm-funil-vendas/)

</div>

**Stack / tópicos:** ``crm`` · ``frontend`` · ``html`` · ``javascript`` · ``kanban`` · ``localstorage`` · ``offline-first`` · ``rest-api`` · ``sales`` · ``sales-funnel`` · ``sales-management`` · ``web-app``

> Projeto mantido por [@mkbraion](https://github.com/mkbraion).
<!-- MKBRAION-POLISH:END -->

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


## Foco do projeto

Este repositório fica dedicado somente ao CRM e ao funil de vendas: cadastro de leads, etapas do funil, valores, conversão, WhatsApp e sincronização opcional entre dispositivos.
