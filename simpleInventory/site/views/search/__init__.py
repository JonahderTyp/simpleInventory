from flask import render_template, Blueprint

search = Blueprint("search", __name__, url_prefix="/search")


@search.route("/")
def index():
    return render_template("search/index.html")
