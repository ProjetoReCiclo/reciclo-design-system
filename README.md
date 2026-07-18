# Design System — Biblioteca de Componentes (Bootstrap 5 + Jinja2 + Flask)

> **Status:** Aprovado para implementação — Parecer Técnico Oficial **DS-001**
> (Supervisor Sênior de Arquitetura e Engenharia de Software), Piloto Pré-MVP.

Biblioteca modular de 11 componentes para montar as ~40 telas do produto por composição de `include`/`import` do Jinja2, sem depender de nenhum framework JS (só Bootstrap 5.3+ Bundle e JS puro).

## Ecossistema RECICLO Design System (§11 do DS-001)

O DS-001 recomenda evoluir de "biblioteca de componentes" para um ecossistema
de 4 bibliotecas independentes. Estrutura já refletida neste pacote:

```
design-system/
├── templates/ + static/          → 1. Biblioteca de Componentes (✅ completa)
├── assets/bootstrap-icons/       → 2. Bootstrap Icons (✅ homologada, via CDN)
├── assets/reciclo-profile-icons/ → 3. RECICLO Profile Icons (⏳ spec pronta, aguarda arte)
└── assets/reciclo-brand-assets/  → 4. RECICLO Brand Assets (⏳ spec pronta, aguarda arte)
```

Cada pasta em `assets/` tem um `README.md` com a especificação de recebimento
(formatos, nomenclatura, tamanhos) para a equipe de Design entregar os
arquivos finais sem ambiguidade.

## Identidade visual — duas camadas

A marca RECICLO usa **dois contextos visuais distintos**, definidos pela equipe de Design:

### Camada 1 — Institucional (`templates/login.html`)
**Retificado:** fundo agora é **branco** (não mais preto) — modelo oficial aprovado
trocou o padrão de alto contraste de preto+dourado para branco+dourado.
Além disso, o emblema central agora **muda por perfil**: cada tela de login
usa o ícone do seu próprio perfil (`static/img/profiles/<slug>.jpg`), em vez
do símbolo genérico RECICLO (R). Teste local:
`/login?perfil=master`, `/login?perfil=motorista`, `/login?perfil=coletor` etc.

| Token | HEX | Uso |
|---|---|---|
| `--ds-inst-bg` / `--ds-inst-bg-panel` | `#ffffff` (Branco oficial) | Fundo da tela e do painel |
| `--ds-inst-gold` | `#c9a227` (Ouro Principal oficial) | Ícone, wordmark, botão |
| `--ds-inst-gold-light` | `#e8c74a` (Ouro Claro oficial) | Gradiente metálico (parte clara) |
| `--ds-inst-gold-matte` | `#8b6914` (Ouro Escuro oficial) | Tagline, texto fosco |
| `--ds-inst-text-dark` | `#1c1a14` (Preto Quente oficial) | Texto escuro (inputs, hover do botão) |

### Camada 2 — Operacional (dashboards, cadastros, operação, auditorias, admin)
Fundo em degradê suave (menta → azul claro), cards brancos, verde para ações, dourado **reservado** para identidade (marca, títulos, indicadores especiais, item de menu ativo) — sem excesso, para preservar a elegância e reduzir fadiga visual.

| Token | Valor | Uso |
|---|---|---|
| `--ds-op-gradient` | `linear-gradient(135deg, #d8fbe7 0%, #c6dcfc 100%)` | Fundo do `<body class="ds-operational">` |
| `--ds-op-green` | `#1e8a4c` | Botão primário (`.btn-primary`), valores positivos |
| `--ds-op-gold` | `#c9962e` | Marca no cabeçalho, título de seção, menu ativo |

## ⚠️ Placeholders aguardando ativos finais da equipe de Design

A paleta acima já é oficial. O que ainda falta plugar:

| Placeholder atual | Onde ajustar quando o ativo chegar |
|---|---|
| Ícone `bi-arrow-repeat` no lugar do símbolo RECICLO | `.ds-login-panel__logo` em `login.html` e `.ds-topbar__brand-icon` em `componentes/cabecalho.html` — trocar `<i>` por `<img src="logo-reciclo.svg">` |
| Inicial do nome em quadrado dourado (`.ds-sidebar__logo`) | Trocar pelo `<img>` do SVG oficial em `componentes/sidebar.html` |
| Avatar genérico (placeholder.com) | Variável `usuario.avatar_url` |

Nenhum componente tem cor "hard-coded" fora do `:root` — qualquer ajuste fino de tom é uma edição no topo de `design-system.css`.

## Estrutura de arquivos

```
design-system/
├── app.py                          # Flask de demonstração (opcional, só para visualizar)
├── static/
│   ├── css/design-system.css       # Tokens (cores, raios, tipografia) + estilos dos 11 componentes
│   └── js/design-system.js         # JS puro: offcanvas mobile, auto-dismiss de alerts, checkbox de tarefas, validação
└── templates/
    ├── base.html                   # Layout mestre — inclui cabeçalho, sidebar, alertas e modais globais
    ├── exemplo_dashboard.html      # Exemplo real de composição de componentes numa tela
    └── componentes/
        ├── cabecalho.html          # 1. Top App Bar
        ├── sidebar.html            # 2. Navigation Rail (desktop) / Bottom Nav (mobile)
        ├── cards_indicadores.html  # 3. Dashboard Cards (KPIs)
        ├── botoes.html             # 4. Vitrine de variantes de botão
        ├── form_inputs.html        # 5. Campos de formulário + validação
        ├── tabelas.html            # 6. Data table responsiva + paginação
        ├── modais.html             # 7. Modal de formulário + modal de confirmação
        ├── alertas.html            # 8. Alerts/Toasts + flash messages do Flask
        ├── badges_status.html      # 9. Macro Jinja2 de badges de status
        ├── cards_pendencias.html   # 10. Task cards
        └── timeline_atividades.html# 11. Activity log
```

## Como montar uma nova tela (as ~40 telas do produto)

```jinja
{% extends 'base.html' %}

{% block titulo %}Título da tela{% endblock %}

{% block conteudo %}
  {% include 'componentes/cards_indicadores.html' %}
  {% include 'componentes/tabelas.html' %}
{% endblock %}
```

O `base.html` já cuida do cabeçalho, da barra lateral responsiva e da área de alertas — a tela só precisa preencher o `block conteudo`.

## Variáveis de contexto que cada componente espera

| Componente | Variável Jinja2 | Formato |
|---|---|---|
| Cabeçalho | `modulo_nome`, `notificacoes_count`, `usuario` | str, int, dict |
| Sidebar | `nav_items` | list de `{endpoint, label, icon}` |
| Cards de Indicadores | `kpis` | list de `{icone, label, valor, tendencia, direcao}` |
| Tabelas | `colunas`, `registros`, `paginacao` | list, list de dict, dict |
| Cards de Pendências | `tarefas` | list de `{id, titulo, prazo, prioridade, concluida}` |
| Timeline | `atividades` | list de `{data_hora, descricao}` |

Recomenda-se centralizar `modulo_nome`, `nav_items` e `usuario` em um `@app.context_processor` do Flask (veja `app.py`), já que são usados em toda tela.

## Rodando a demo localmente

```bash
pip install flask
python app.py
# abrir http://127.0.0.1:5000
```

## Responsividade (baseado em Material Design)

- **Mobile (<992px):** barra lateral vira Bottom Navigation Bar fixa no rodapé (4 destinos principais) + drawer offcanvas para os demais itens, acionado pelo botão hambúrguer do cabeçalho.
- **Desktop (≥992px):** Navigation Rail compacta fixa à esquerda; cabeçalho e conteúdo se deslocam automaticamente (`margin-left`) para não ficar por baixo da rail.

## Convenções de nomenclatura CSS

Todas as classes customizadas usam o prefixo `ds-` (Design System) para nunca colidir com as classes nativas do Bootstrap — ex.: `.ds-topbar`, `.ds-kpi-card`, `.ds-timeline`.
