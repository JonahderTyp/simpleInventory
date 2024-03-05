from flask import Flask
from pathlib import Path
#from .api import api
from sqlalchemy.schema import CreateTable
import logging

def print_sql_creation_script(db):
    engine = db.get_engine()
    for table in db.Model.metadata.tables.values():
        print(CreateTable(table).compile(engine))

print("Hello from Init Script")
logging.basicConfig(level=logging.DEBUG)

def create_app():


    app = Flask(__name__)


    db_path = Path(app.instance_path)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path.absolute()}'
    app.config['FLASK_DB_SEEDS_PATH'] = (Path(app.root_path) / "./seeds.py").absolute()
    #app.config['SQLALCHEMY_ECHO'] = True  # Enable echoing of SQL statements
    
    from simpleInventory.database import db

    db.init_app(app)


    from . import api, site
    app.register_blueprint(api)
    app.register_blueprint(site)

    return app
