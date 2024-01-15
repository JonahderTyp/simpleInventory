from flask import render_template, request, redirect, url_for, abort
from ...database.handel import *
from flask import Blueprint

item_site = Blueprint("item", __name__, template_folder="../templates/item/", url_prefix="/item")

@item_site.route("/", methods=["GET"])
def index():
    print("rendering Item Index")
    return render_template("item/index.html")

@item_site.route("/<int:itemID>", methods=["GET"])
def showItem(itemID):
    item = getItem(itemID)
    return render_template("item/item.html", item=item)