from . import db
from .json_encoder import DatabaseEncoder
from .db import Item, Storage
from datetime import datetime as dt
from .exceptions import *
from pprint import pprint
from sqlalchemy import desc
import logging

def getItem(itemID):
    return {"id":itemID, "name":"placeholder"}

def getGrandStorage():
    storages_without_parent = Storage.query.filter(Storage.parent_id == None).all()
    return storages_without_parent

def getChildStorages(parent_id):
    # Query to find all child storages of the given parent storage
    child_storages = Storage.query.filter_by(parent_id=parent_id).all()
    return child_storages

def createChildStorage(name, parent_id):
    logging.debug(f"Creating Storage parent:{parent_id}, name:{name}")
    child_storage = Storage(name=name, parent_id=parent_id)
    db.session.add(child_storage)
    db.session.commit()
    return child_storage

def getStorageByID(storage_id):
    # Query the database for the Storage object with the specified id
    storage = Storage.query.filter_by(id=storage_id).first()
    return storage

def getAll():
    return Storage.query.all()

def delete_storage(storage_id):
    # Find the storage record by its ID
    storage = Storage.query.get(storage_id)

    if storage is None:
        raise ElementDoesNotExsist()

    # Delete all items associated with the storage
    # for item in storage.items:
    #     db.session.delete(item)

    # Delete the storage record
    db.session.delete(storage)
    
    # Commit the changes to the database
    db.session.commit()

    return