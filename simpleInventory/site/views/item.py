from flask import render_template, request, redirect, url_for, abort
from ...database.handel import *
from flask import Blueprint

item_site = Blueprint("item", __name__, template_folder="../templates/item", url_prefix="/item")

# ... (your existing team-related routes go here)

@item_site.route("/")
def showAllItems():
    return render_template("index.html")

@item_site.route("/<int:itemID>", methods=["POST"])
def showItem(itemID):
    item = getItem(itemID)
    return render_template("item.html", item=item)