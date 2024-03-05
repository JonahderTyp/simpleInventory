from . import db
from .db import Item, Storage
from .exceptions import ElementAlreadyExists, ElementDoesNotExsist
from pprint import pprint
from sqlalchemy import desc
from sqlalchemy.orm import joinedload

def create_storage(name, parent_id=None):
    new_storage = Storage(name=name, parent_id=parent_id)
    db.session.add(new_storage)
    db.session.commit()
    return new_storage

def delete_storage(storage_id):
    storage = Storage.query.get(storage_id)
    if storage and not storage.items.all() and all(not child.items.all() for child in storage.children):
        db.session.delete(storage)
        db.session.commit()
        return True
    return False

def get_items_with_paths(storage_id):
    items_with_paths = []
    storage = Storage.query.options(joinedload(Storage.items)).get(storage_id)

    def get_path(storage, path=[]):
        if storage.parent:
            return get_path(storage.parent, [storage.name] + path)
        else:
            return [storage.name] + path

    if storage:
        for item in storage.items:
            item_path = " -> ".join(get_path(storage))
            items_with_paths.append((item.name, item_path))
    return items_with_paths

def create_item(name, description, storage_id):
    new_item = Item(name=name, description=description, storage_id=storage_id)
    db.session.add(new_item)
    db.session.commit()
    return new_item

def delete_item(item_id):
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return True
    return False

def edit_item(item_id, name=None, description=None):
    item = Item.query.get(item_id)
    if item:
        if name:
            item.name = name
        if description:
            item.description = description
        db.session.commit()
        return item
    return None