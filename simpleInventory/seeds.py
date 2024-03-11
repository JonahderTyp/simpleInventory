
from simpleInventory.database.db import db, Item, Storage


def add_storage(name, parent_id=None):
    storage = Storage(name=name, parent_id=parent_id)
    print(storage.get_model_dict())
    db.session.add(storage)
    db.session.commit()
    return storage

def add_item(name, description, storage):
    item = Item(name=name, description=description, storage=storage)
    db.session.add(item)
    return item


def create_storage_tree(parent_id=None, layer=1, max_layers=5):
    """
    Recursively creates a tree of Storages.

    :param parent_id: The parent ID for the storage. None for the root.
    :param layer: Current layer in the tree.
    :param max_layers: The total number of layers to create.
    """
    if layer > max_layers:
        return
    for i in range(3):  # Create 3 storages per layer
        storage_name = f"Storage Layer {layer} - Storage {i + 1}"
        storage = add_storage(storage_name, parent_id=parent_id)
        for j in range(3):  # Add 3 items to each storage
            item_name = f"Item for {storage_name} - Item {j + 1}"
            add_item(item_name, f"Description for {item_name}", storage)
        create_storage_tree(storage.id, layer + 1, max_layers)


def seed_data():
    """Seeds the database with initial test data."""
    print("seeding Data...")
    db.session.commit()  # Commit any pending transactions
    # db.drop_all()  # Be cautious, this will delete all existing data
    # db.create_all()  # Create tables based on models

    # Create storages
    # storage1 = add_storage('Main Storage')
    # print(storage1.id)
    # storage2 = add_storage('Sub Storage 1', parent_id=storage1.id)
    # storage3 = add_storage('Sub Storage 2', parent_id=storage1.id)

    # # Create items
    # add_item('Item 1', 'Description for Item 1', storage1)
    # add_item('Item 2', 'Description for Item 2', storage2)
    # add_item('Item 3', 'Description for Item 3', storage3)
    
    create_storage_tree()

    # Commit changes to database
    db.session.commit()
    
    print("Data seeded successfully.")

    