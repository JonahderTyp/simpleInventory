from .db import db, Item, Storage
from .exceptions import ElementAlreadyExist, ElementDoesNotExist, ElementIsNotEmpty
from typing import List, Dict, Any


def create_storage(name: str, parent_id: int | None = None) -> Storage:
    """
    Creates a new Storage entity and persists it to the database.

    This function creates a new Storage object with a specified name and,
    optionally, a parent ID for hierarchical organization. After creation,
    the new storage entity is added to the session and committed to the database,
    making the changes permanent.

    Parameters:
    - name (str): The name of the new storage entity. This is a required parameter.
    - parent_id (int, optional): The ID of the parent storage entity, if the new storage
      is to be a child in a hierarchical structure. Defaults to None, indicating
      that the new storage has no parent (i.e., it is a top-level storage entity).

    Returns:
    - Storage: The newly created Storage object, now persisted in the database.

    Note:
    - The function assumes that the necessary database session (db.session) is already
      established and will directly commit changes to the database. Make sure to handle
      any potential exceptions that might arise from database operations outside this function.
    """
    new_storage = Storage(name=name, parent_id=parent_id)
    db.session.add(new_storage)
    db.session.commit()
    return new_storage


def delete_storage(storage_id: int) -> bool:
    """
    Attempts to delete a storage entity based on its ID.

    Args:
    - storage_id (int): The ID of the storage to be deleted.

    Raises:
    - ElementDoesNotExsist: If the specified storage does not exist.
    - ElementIsNotEmpty: If the storage or any of its children have associated items.

    Returns:
    - True: if the storage was successfully deleted.
    """
    storage = Storage.query.get(storage_id)
    if not storage:
        raise ElementDoesNotExist(f"Storage {storage_id} does not exitst.")

    if storage.items.all() or any(child.items.all() for child in storage.children):
        raise ElementIsNotEmpty(
            f"Storage {storage_id} or its children have associated items and cannot be deleted.")

    db.session.delete(storage)
    db.session.commit()
    return True


def search_storages(query: str) -> List[Storage]:
    """
    Searches for storages by name or id.

    Args:
        query (str): The search query string.

    Returns:
        List[Storage]: A list of Storage objects that match the search query in their name.
    """
    search = f"%{query}%"
    storages = Storage.query.filter(Storage.id.ilike(
        search) | Storage.name.ilike(search)).all()
    return storages


def get_root_storages() -> List[Dict[str, Any]]:
    """
    Fetches all Storage records that do not have a parent.

    :return: List of Storage instances that are root nodes (having no parent).
    """
    root_storages: List[Storage] = Storage.query.filter(
        Storage.parent_id == None).all()
    return [get_storage_hierarchy(i.id) for i in root_storages]


def get_storage_hierarchy(storage_id: int) -> Dict[str, Any]:
    """
    Fetches a storage by its ID and returns its parent, the storage itself, and its children.

    Args:
    - storage_id (int): ID of the storage to find.

    Returns:
        Dict: Dictionary containing the parent, the storage itself, and its children.
    """
    storage: Storage
    storage = Storage.query.get(storage_id)
    if not storage:
        raise ElementDoesNotExist

    # Fetch parent
    parent: Storage | None = None
    if storage.parent_id:
        parent = Storage.query.get(storage.parent_id)

    # Fetch children
    children: List[Storage] = Storage.query.filter_by(
        parent_id=storage_id).all()

    # Preparing the result with parent, self, and children information
    result = {
        "self": storage.get_model_dict(),
        "parent": parent.get_model_dict() if parent else None,
        "children": [child.get_model_dict() for child in children]
    }

    return result


def create_item(name: str, description: str, storage_id: int | None = None) -> Item:
    """
    Create an Item.

    Args:
    - name (str): Name of the Item.
    - description (str): Description of the Item.
    - storage_id (int | None, optional): Items Initial Location. Defaults to None.

    Returns:
    - Item: The created Item.
    """
    if storage_id is not None and isinstance(storage_id, int):
        # Check if a storage exists for the given storage_id
        storage = Storage.query.get(storage_id)
        if storage is None:
            raise ElementDoesNotExist(f"No storage found for ID {storage_id}")
    new_item = Item(name=name, description=description, storage_id=storage_id)
    db.session.add(new_item)
    db.session.commit()
    return new_item


def get_item_by_id(item_id: int) -> Item:
    """
    Retrieve an item entity by its ID.

    Args:
    - item_id (int): ID of the item to retrieve.

    Returns:
    - Item: The retrieved Item object.

    Raises:
    - ElementDoesNotExist: If no Item with the specified ID exists.
    """
    item = Item.query.get(item_id)
    if not item:
        raise ElementDoesNotExist(f"Item {item_id} does not exitst.")
    return item


def edit_item(item_id: int, name: str | None = None, description: str | None = None) -> Item:
    """
    Update properties of an item entity.

    Args:
    - item_id (int): The ID of the item to update.
    - name (str, optional): New name for the item. If None, the name will not be changed.
    - description (str, optional): New description for the item. If None, the description will not be changed.

    Returns:
    - Item: The updated Item object.

    Raises:
    - ElementDoesNotExist: If no Item with the specified ID exists.
    """

    item = Item.query.get(item_id)
    if not item:
        raise ElementDoesNotExist(f"Item {item_id} does not exitst.")
    if name:
        item.name = name
    if description:
        item.description = description
    db.session.commit()
    return item


def delete_item(item_id: int) -> bool:
    """
    Attempts to delete an item entity based on its ID.

    Args:
    - item_id (int): The ID of the item to be deleted.

    Returns:
    - bool: True if the item was successfully deleted, False otherwise.

    Raises:
    - ElementDoesNotExist: If no Item with the specified ID exists.
    """
    item = Item.query.get(item_id)
    if not item:
        raise ElementDoesNotExist(f"Item {item_id} does not exitst.")
    db.session.delete(item)
    db.session.commit()
    return True


def search_items(query: str) -> List[Item]:
    """
    Searches for items by id, name and description.

    Args:
        query (str): The search query string.

    Returns:
        List[Item]: A list of Item objects that match the search query in either name or description.
    """
    search = f"%{query}%"
    items = Item.query.filter(
        (Item.id.ilike(search)) | (Item.name.ilike(search)) | (
            Item.description.ilike(search))
    ).all()
    return items
