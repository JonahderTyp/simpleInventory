# site/views/overview.py
from flask import render_template, request, redirect, url_for
from ...database.handel import *
from .tools import formatDatetime
from flask import Blueprint
from pprint import pprint
import time
from datetime import datetime


overview_site = Blueprint("overview", __name__, template_folder="../templates/overview", url_prefix="/overview")

@overview_site.route("/")
def showOverview():
    return render_template("overview/index.html")

