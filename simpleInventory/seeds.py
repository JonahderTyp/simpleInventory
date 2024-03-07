
from simpleInventory.database.db import db, Item, Storage


def add_storage(name, parent_id=None):
    storage = Storage(name=name, parent_id=parent_id)
    db.session.add(storage)
    return storage

def add_item(name, description, storage):
    item = Item(name=name, description=description, storage=storage)
    db.session.add(item)
    return item

def seed_data():
    """Seeds the database with initial test data."""
    db.session.commit()  # Commit any pending transactions
    # db.drop_all()  # Be cautious, this will delete all existing data
    # db.create_all()  # Create tables based on models

    # Create storages
    storage1 = add_storage('Main Storage')
    storage2 = add_storage('Sub Storage 1', parent_id=storage1.id)
    storage3 = add_storage('Sub Storage 2', parent_id=storage1.id)

    # Create items
    add_item('Item 1', 'Description for Item 1', storage1)
    add_item('Item 2', 'Description for Item 2', storage2)
    add_item('Item 3', 'Description for Item 3', storage3)

    # Commit changes to database
    db.session.commit()
    