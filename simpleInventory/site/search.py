from flask import render_template, Blueprint, request
from ..database import handel as db

search = Blueprint("search", __name__, url_prefix="/search")


@search.route("/")
def index():
    results = []
    query = request.args.get('query', None)
    if query is not None:
        for item in db.search_items(query):
            data = item.get_model_dict()
            data.update({
                "path":db.get_path_of_storage(db.get_storage_by_id(data.get('storage_id')))
            })
            results.append(data)
    return render_template("search/index.html", results=results)
