from flask import render_template, Blueprint

browse = Blueprint("browse", __name__, url_prefix="/browse")


@browse.route("/")
def index():
    return render_template("browse/index.html")
