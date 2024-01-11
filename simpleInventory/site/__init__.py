from flask import Blueprint, render_template
from .views import overview, item

site = Blueprint("site", __name__, template_folder="templates")


#site.register_blueprint(task_views.tasks_site)
#site.register_blueprint(team_views.teams_site)
site.register_blueprint(overview.overview_site)
site.register_blueprint(item.item_site)


@site.route("/")
def index():
    return render_template("index.html")