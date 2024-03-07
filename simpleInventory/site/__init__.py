from flask import Blueprint, render_template

from .search import search
from .browse import browse

site = Blueprint("site", __name__, template_folder="templates")


site.register_blueprint(browse)
site.register_blueprint(search)


@site.route("/")
def index():
    return render_template("index.html")