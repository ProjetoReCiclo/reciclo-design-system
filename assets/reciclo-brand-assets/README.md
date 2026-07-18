# RECICLO Brand Assets — Spec de Recebimento

Referência: DS-001, §10 e §11. Biblioteca institucional da marca — separada
da biblioteca de componentes e dos ícones funcionais.

## Itens obrigatórios (conforme §10)

| Item | Formato | Observações |
|---|---|---|
| Logotipo — versão positiva | `.svg` + `.png` (≥3000×3000px) | Fundo transparente |
| Logotipo — versão negativa | `.svg` + `.png` (≥3000×3000px) | Fundo transparente |
| Logotipo — versão monocromática | `.svg` + `.png` (≥3000×3000px) | Fundo transparente |
| Ícone institucional (favicon / apps móveis) | `.svg` + `.png` (múltiplos tamanhos: 16, 32, 180, 512px) | Já usado como recorte do logo |
| Paleta oficial | HEX + RGB | Ver proposta já em uso em `static/css/design-system.css` (`--ds-inst-*` e `--ds-op-*`) — confirmar ou ajustar |
| Manual simplificado de aplicação da marca | PDF ou Markdown | Área de proteção, tamanho mínimo, usos incorretos |

## Onde os arquivos entram no projeto, assim que chegarem

```
assets/reciclo-brand-assets/
├── logo-positiva.svg
├── logo-positiva.png
├── logo-negativa.svg
├── logo-negativa.png
├── logo-monocromatica.svg
├── favicon/
│   ├── favicon-16.png
│   ├── favicon-32.png
│   ├── apple-touch-icon-180.png
│   └── icon-512.png
└── manual-marca.pdf
```

## Pontos de substituição no código (já sinalizados no Design System)

| Onde está hoje (placeholder) | Trocar por |
|---|---|
| `<i class="bi bi-arrow-repeat">` em `templates/login.html` | `<img src="logo-positiva.svg" class="ds-login-panel__logo">` |
| `<i class="bi bi-arrow-repeat">` em `templates/componentes/cabecalho.html` | `<img src="logo-branca-dourada.svg" class="ds-topbar__brand-icon">` |
| Inicial do nome em `.ds-sidebar__logo` (`componentes/sidebar.html`) | `<img src="favicon/icon-512.png">` ou recorte do símbolo |
| Tokens de cor em `:root` (`design-system.css`) | Confirmar/ajustar HEX conforme paleta oficial final |

## Status atual

🟢 **Logotipo recebido em 2 variantes** e já integrado:
`static/img/brand/logo-reciclo-r.jpg` (monograma "R", em uso no cabeçalho, na
sidebar e na tela de Login) e `logo-reciclo-gota.jpg` (símbolo da gota de
óleo, disponível como alternativa). Cópia bruta também em
`assets/reciclo-brand-assets/recebido/`.

⚠️ **Ainda não atende à spec original desta pasta:** os arquivos são `.jpg`
com fundo preto, não `.svg`/`.png` em fundo transparente ≥3000×3000px. Por
ora isso funciona porque o Design System usa o logo como "medalhão" circular
(fundo preto + borda dourada via CSS), mas essa solução não escala para todo
uso possível da marca (ex.: impressão, favicon em fundo colorido, aplicações
fora do padrão circular). O restante da lista (versão negativa formal,
monocromática isolada, favicon em múltiplos tamanhos, manual de aplicação)
continua pendente.
