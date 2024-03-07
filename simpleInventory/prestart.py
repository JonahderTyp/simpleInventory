from pathlib import Path
from simpleInventory import create_app
from simpleInventory.database import db
from .seeds import seed_data


def pre_start():
    app = create_app()
    with app.app_context():
        db_path = Path(app.instance_path)
        if not db_path.is_file():
            print(f"Seeding database at {db_path.absolute()}")
            db.create_all()
            seed_data()