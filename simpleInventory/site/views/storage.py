from flask import render_template, request, redirect, url_for, abort
from ...database.handel import *
from flask import Blueprint

storage_site = Blueprint("storage", __name__, template_folder="../templates/storage/", url_prefix="/storage")


@storage_site.route("/", methods=["GET"])
def index():
    grandStorage = getGrandStorage()
    print(grandStorage)
    return render_template("storage/index.html", grandStorage = grandStorage, items = None)

@storage_site.route("/<int:storageID>", methods=["GET"])
def showID(storageID):
    parent = getStorageByID(storageID)
    children = getChildStorages(storageID)
    return render_template("storage/storage.html", children = children, parent = parent, items = None)

@storage_site.route("/create", methods=["GET", "POST"])
@storage_site.route("/<int:storageID>/create", methods=["GET", "POST"])
def create(storageID = None):
    error_message = None
    form_data = {"name":"", "parent": storageID}
    if request.method == "POST":
        try:
            print(request.form)
            form_data["name"] = request.form.get("name")
            
            if request.form.get("parent") is "":
                form_data["parent"] = None
            else:
                form_data["parent"] = int(request.form.get("parent"))
            
            createChildStorage(form_data["name"], form_data["parent"])
        except Exception as ex:
            error_message = str(ex)

    return render_template("storage/create.html", error_message=error_message, form_data = form_data, isActive = "readonly" if storageID else "")

@storage_site.route("/all", methods=["GET"])
def all():
    storages = getAll()
    return render_template("storage/all.html", storages = storages)