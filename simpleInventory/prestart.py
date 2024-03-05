from pathlib import Path
from simpleInventory import create_app
from simpleInventory.database import db


def pre_start():
    app = create_app()
    with app.app_context():
        db_path = Path(app.instance_path)
        if not db_path.is_file():
            print(f"Seeding database at {db_path.absolute()}")
            db.create_all()
            seeds_path = app.config.get("FLASK_DB_SEEDS_PATH")
            if Path.exists(seeds_path):
                exec(open(seeds_path).read())
            else:
                print("Could not seed database because of a missing file")