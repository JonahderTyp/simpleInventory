from flask import render_template, Blueprint, request
from ..database.db import Storage, Item
from ..database.json_encoder import DatabaseEncoder
from ..database import handel as db
from typing import List
from pprint import pprint

browse = Blueprint("browse", __name__, url_prefix="/browse")

@browse.route("/")
def index():
    children = []
    for storages in db.get_root_storages():
        children.append(storages.get('storage'))
    items = db.get_items_by_storage(None)
    return render_template("browse/index.html",
                           children=DatabaseEncoder.default(children),
                           items=DatabaseEncoder.default(items))


@browse.route("/<int:storage_id>")
def look(storage_id):
    infos = DatabaseEncoder.default(db.get_storage_hierarchy(storage_id))
    items = db.get_items_by_storage(storage_id)
    return render_template("browse/index.html",
                           parent=infos['parent'],
                           storage=infos['storage'],
                           children=infos['children'],
                           items=DatabaseEncoder.default(items))
