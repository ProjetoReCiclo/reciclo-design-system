# Bootstrap Icons — Biblioteca Oficial de Ícones Funcionais

Referência: DS-001, §8. Homologada como **única** biblioteca de ícones
funcionais da interface (dashboard, formulários, tabelas, navegação, etc.).

- CDN em uso: `https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css`
  (já incluído em `templates/base.html` e `templates/login.html`)
- Uso: `<i class="bi bi-nome-do-icone"></i>`
- **Não misturar com outras bibliotecas de ícones** (Font Awesome, Feather,
  Material Icons etc.) — nenhum componente do Design System usa outra fonte
  de ícone além desta.
- Os únicos elementos com identidade própria (fora do Bootstrap Icons) são os
  **RECICLO Profile Icons** (`assets/reciclo-profile-icons/`) e os
  **RECICLO Brand Assets** (`assets/reciclo-brand-assets/`) — esses são
  ativos institucionais, não ícones funcionais de interface.

Nenhum arquivo precisa ser baixado: a biblioteca é consumida via CDN.
