from flask import Blueprint, render_template

from db.db import DbOperations
from utils.bubble_sort import bubble_sort

teams_blueprint = Blueprint("teams", __name__, url_prefix="/")


@teams_blueprint.route("/")
def index_view():
    with DbOperations() as db:
        teams = db.get_clubes()
    return render_template("index.html", equipas=teams)


@teams_blueprint.route("/sobre")
def sobre_view():
    return render_template("sobre.html")


@teams_blueprint.route("/ordenar/<index>")
def ordenar_view(index: int):
    index = int(index)
    with DbOperations() as db:
        teams = db.get_clubes()
    lista_ordenada = bubble_sort(teams, index)
    return render_template("ordenar.html", lista_ordenada=lista_ordenada)
