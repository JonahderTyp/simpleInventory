from flask import Flask
from pathlib import Path
from .site import site
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

    from simpleInventory.database import db

    db_path = Path(app.instance_path)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path.absolute()}'
    app.config['FLASK_DB_SEEDS_PATH'] = (Path(app.root_path) / "./seeds.py").absolute()
    #app.config['SQLALCHEMY_ECHO'] = True  # Enable echoing of SQL statements

    print(db_path)

    NEW_DB = not Path.is_file(db_path)

    db.init_app(app)

    print(f"is new DB: {NEW_DB}")
    

    if NEW_DB:
        with app.app_context():
            print_sql_creation_script(db)
            app.logger.info(f"Seeding database at {db_path.absolute()}")
            db.create_all()
            seeds_path = app.config.get("FLASK_DB_SEEDS_PATH")
            if Path.exists(seeds_path):
                exec(open(seeds_path).read())
            else:
                app.logger.error("Could not seed database because of a missing file")
    else:
        print("DB already created")

    app.register_blueprint(site)
    #app.register_blueprint(api)

    return app
