from flask import Blueprint, render_template
from .views import browse, search

site = Blueprint("site", __name__, template_folder="templates")


site.register_blueprint(browse.browse)
site.register_blueprint(search.search)


@site.route("/")
def index():
    print("rendering main index")
    return render_template("index.html")