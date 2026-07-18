# RECICLO Profile Icons — Spec de Recebimento

Referência: DS-001, §9. Biblioteca institucional dos **perfis operacionais** da
plataforma. Não deve usar Bootstrap Icons — são ativos de marca, com
identidade própria.

## Perfis previstos (8)

1. Administrador Master
2. Operador Logístico
3. Coletor
4. Motorista
5. Gerador
6. Representante Comercial
7. Auditor
8. Destinador

## Variantes obrigatórias por perfil

Cada um dos 8 perfis acima deve ser entregue em **5 arquivos SVG**:

| Sufixo do arquivo | Variante |
|---|---|
| `-colorida.svg` | Versão colorida (uso padrão) |
| `-branca.svg` | Versão branca (para fundos escuros/coloridos) |
| `-dourada.svg` | Versão dourada (Camada Institucional) |
| `-mono.svg` | Versão monocromática (1 cor, herda `currentColor`) |
| `-outline.svg` | Versão colorida "cheia", usada como base das demais |

Total esperado: **40 arquivos SVG** (8 perfis × 5 variantes).

## Convenção de nomenclatura

```
assets/reciclo-profile-icons/
├── admin-master/
│   ├── admin-master-colorida.svg
│   ├── admin-master-branca.svg
│   ├── admin-master-dourada.svg
│   ├── admin-master-mono.svg
│   └── admin-master-outline.svg
├── operador-logistico/
├── coletor/
├── motorista/
├── gerador/
├── representante-comercial/
├── auditor/
└── destinador/
```

## Requisitos técnicos do SVG

- `viewBox` consistente entre todos os ícones (ex.: `0 0 48 48`), para que o
  tamanho seja intercambiável entre perfis sem distorcer.
- Versão `-mono.svg` deve usar `fill="currentColor"` em todos os paths, para
  herdar a cor via CSS (`color: var(--ds-op-gold)`, por exemplo).
- Sem texto embutido no SVG (nomes de perfil ficam no HTML/Jinja2, não na arte).
- Peso de arquivo otimizado (rodar por um otimizador tipo SVGO antes de entregar).

## Como cada perfil deve ser integrado ao Design System (dev)

Assim que os arquivos chegarem em `assets/reciclo-profile-icons/<perfil>/`,
o front-end vai referenciá-los via Jinja2, por exemplo:

```jinja
<img src="{{ url_for('static', filename='profile-icons/coletor/coletor-colorida.svg') }}"
     alt="Perfil: Coletor" width="32" height="32">
```

(os arquivos finais devem ser copiados para `static/profile-icons/` no projeto Flask)

## Status atual

🟢 **6 ícones recebidos e já integrados** ao Design System em
`static/img/profiles/`: `cooperativa.jpg`, `refinaria.jpg`, `destinatario.jpg`,
`coletor.jpg`, `gerador.jpg`, `transportador.jpg`. Uma cópia bruta também fica
em `assets/reciclo-profile-icons/recebido/` para referência/histórico.

⚠️ **Ponto de atenção — nomenclatura difere do DS-001 §9.** O parecer técnico
previa 8 perfis (Administrador Master, Operador Logístico, Coletor, Motorista,
Gerador, Representante Comercial, Auditor, Destinador). Os ativos recebidos
trazem 6 perfis com nomes diferentes: **Cooperativa** e **Refinaria** (novos,
não previstos), **Destinatário** (não "Destinador"), **Transportador** (não
"Motorista"). Não recebemos ícones para Administrador Master, Operador
Logístico, Representante Comercial nem Auditor.
→ Confirmar com a liderança se a lista de perfis mudou (e os 4 que faltam não
existem mais) ou se esses 4 ainda vão ser entregues com nomes próprios.

⚠️ **Formato recebido:** `.jpg` com fundo preto (não é o `.svg` transparente
da spec original desta pasta). Isso funciona bem como "medalhão" circular
(fundo preto + borda dourada, via CSS `border-radius: 50%`), que é como o
badge de perfil (`componentes/perfil_badge.html`) já está implementado. Se a
equipe de Design ainda for entregar versões vetoriais/transparentes depois,
os `src` dos `<img>` no template continuam sendo o único ponto de troca.
