from flask import render_template, request, redirect, url_for, abort
from ..database import handel as db
from ..database.json_encoder import DatabaseEncoder
from flask import Blueprint

item = Blueprint("item", __name__, url_prefix="/item")


@item.route("/", methods=["GET"])
def index():
    print("rendering Item Index")
    return render_template("item/index.html")


@item.route("/<int:itemID>", methods=["GET"])
def showItem(itemID):
    item = db.get_item_by_id(itemID)
    storage = db.get_storage_by_id(item.storage_id)
    path = db.get_path_of_storage(storage)
    return render_template("item/item.html",
                           item=DatabaseEncoder.default(item),
                           storage=DatabaseEncoder.default(storage),
                           path=DatabaseEncoder.default(path))
