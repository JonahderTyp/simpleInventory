from flask import render_template, Blueprint, request
from ..database import handel as db

search = Blueprint("search", __name__, url_prefix="/search")


@search.route("/")
def index():
    results = []
    query = request.args.get('query', None)
    if query is not None:
        results = [i.get_model_dict() for  i in db.search_items(query)]
    return render_template("search/index.html", results=results)
