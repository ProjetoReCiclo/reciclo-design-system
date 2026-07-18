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

⚠️ **Novo pedido pendente:** o emblema do Login agora é padronizado em
28–32px (spec aprovada com a liderança), com o wordmark "RECICLO" tipografado
separadamente em HTML (`.ds-login-panel__brand`). Nesse tamanho, o texto
"RECICLO" que já vem cravado nos arquivos `logo-reciclo-r.jpg` /
`logo-reciclo-gota.jpg` fica ilegível (redundância inofensiva, mas não ideal).
Se possível, pedir à equipe de Design uma versão **apenas do ícone, sem o
texto embutido** — melhora a nitidez do emblema pequeno e facilita reuso em
outros tamanhos (favicon, sidebar, etc.).
