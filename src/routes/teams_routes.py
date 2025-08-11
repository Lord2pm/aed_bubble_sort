from flask import Blueprint, render_template

from db.db import DbOperations

teams_blueprint = Blueprint("teams", __name__, url_prefix="/")


@teams_blueprint.route("/")
def index():
    with DbOperations() as db:
        teams = db.get_clubes()
    print(teams)
    return render_template("index.html", equipas=teams)


@teams_blueprint.route("/sobre")
def sobre():
    return render_template("sobre.html")


"""
@teams_blueprint.route("/ordenar/<id>")
def ordenar(id):
    dados = model.get_clubes()
    lista_nomes = []
    lista_orcamentos = []
    lista_titulos = []

    for dado in dados:
        lista_nomes.append(dado[1])
        lista_orcamentos.append(dado[2])
        lista_titulos.append(dado[3])

    if id == "1":
        titulo = "ordenadas de A - Z"
        lista_ordenada = bubble_sort(lista_nomes)
        campo = "nome"
    elif id == "2":
        lista_orcamentos = list(set(lista_orcamentos))
        lista_ordenada = bubble_sort(lista_orcamentos)
        titulo = "dispostas pelos seus orçamentos"
        campo = "orcamento"
    else:
        lista_titulos = list(set(lista_titulos))
        lista_ordenada = bubble_sort(lista_titulos)
        others = model.get_clube("orcamento", dado)
        titulo = "dispostas pela quantidade de títulos"
        campo = "qtd_titulos"

    return render_template(
        "ordenar.html",
        model=model,
        lista_ordenada=lista_ordenada,
        titulo=titulo,
        campo=campo,
    )
"""
