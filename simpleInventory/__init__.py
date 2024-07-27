import os
from flask import Flask
from pathlib import Path
# from .api import api
from sqlalchemy.schema import CreateTable
import logging


def print_sql_creation_script(db):
    engine = db.get_engine()
    for table in db.Model.metadata.tables.values():
        print(CreateTable(table).compile(engine))


def create_app():
    INSTANCE_PATH = os.path.abspath(os.path.join(
        os.path.abspath(__path__[0]), "../instance"))

    app = Flask(__name__, instance_path=INSTANCE_PATH)

    config_path = Path(app.instance_path) / "config.cfg"

    if config_path.is_file():
        app.config.from_pyfile(config_path)
    else:
        logging.warning(
            f"No config file found at {config_path}. Using default config.")

    from .database import db
    from .database.seeds import seed_database
    db.init_app(app)

    with app.app_context():
        db.create_all()

        NEW_DB = all(db.session.query(table).first()
                     is None for table in db.metadata.sorted_tables)

        if NEW_DB:
            seed_database()

    from .api import api
    from .site import site
    app.register_blueprint(api)
    app.register_blueprint(site)

    return app
