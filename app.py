"""
App Flask mínimo apenas para DEMONSTRAR o Design System.
Rode com: python app.py  (requer Flask instalado: pip install flask)
As 40 telas reais do produto devem seguir o mesmo padrão de contexto usado aqui.
"""
from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "troque-esta-chave-em-producao"

NAV_ITEMS = [
    {"endpoint": "dashboard", "label": "Início", "icon": "bi-house"},
    {"endpoint": "clientes", "label": "Clientes", "icon": "bi-people"},
    {"endpoint": "relatorios", "label": "Relatórios", "icon": "bi-bar-chart"},
    {"endpoint": "configuracoes", "label": "Config.", "icon": "bi-gear"},
]


def contexto_base():
    return {
        "modulo_nome": "NomeApp",
        "nav_items": NAV_ITEMS,
        "notificacoes_count": 3,
        "usuario": {"nome": "Maria Souza", "avatar_url": None},
    }


@app.context_processor
def inject_globals():
    return contexto_base()


@app.route("/login")
def login():
    return render_template("login.html", perfil_nome="COLETOR")


@app.route("/")
def dashboard():
    kpis = [
        {"icone": "bi-cash-stack", "label": "Faturamento Mensal", "valor": "R$ 128.400", "tendencia": 12.4, "direcao": "up"},
        {"icone": "bi-people", "label": "Novos Clientes", "valor": "342", "tendencia": 4.1, "direcao": "up"},
        {"icone": "bi-cart-x", "label": "Cancelamentos", "valor": "18", "tendencia": 2.3, "direcao": "down"},
        {"icone": "bi-clock-history", "label": "Tempo Médio", "valor": "3,2 dias", "tendencia": 1.8, "direcao": "down"},
    ]

    colunas = ["Nome", "E-mail", "Status", "Data de cadastro"]
    registros = [
        {"id": 1, "nome": "João Pereira", "email": "joao@exemplo.com",
         "status_html": '<span class="ds-badge-status bg-warning-subtle text-warning-emphasis"><i class="bi bi-clock-fill"></i> Pendente</span>',
         "data": "12/07/2026"},
        {"id": 2, "nome": "Ana Lima", "email": "ana@exemplo.com",
         "status_html": '<span class="ds-badge-status bg-success-subtle text-success-emphasis"><i class="bi bi-check-circle-fill"></i> Concluído</span>',
         "data": "10/07/2026"},
    ]
    paginacao = {"pagina_atual": 1, "total_paginas": 3}

    tarefas = [
        {"id": 1, "titulo": "Aprovar orçamento do trimestre", "prazo": "20/07", "prioridade": "alta", "concluida": False},
        {"id": 2, "titulo": "Revisar contrato do fornecedor", "prazo": "22/07", "prioridade": "media", "concluida": False},
    ]

    atividades = [
        {"data_hora": "18/07/2026 14:32", "descricao": "João Pereira criou o registro #4521"},
        {"data_hora": "18/07/2026 09:15", "descricao": "Sistema gerou o relatório mensal automaticamente"},
    ]

    return render_template(
        "exemplo_dashboard.html",
        kpis=kpis, colunas=colunas, registros=registros, paginacao=paginacao,
        tarefas=tarefas, atividades=atividades,
    )


@app.route("/clientes")
def clientes():
    flash("Cliente salvo com sucesso!", "success")
    return redirect(url_for("dashboard"))


@app.route("/relatorios")
def relatorios():
    return "Página de relatórios (placeholder)"


@app.route("/configuracoes")
def configuracoes():
    return "Página de configurações (placeholder)"


if __name__ == "__main__":
    app.run(debug=True)
