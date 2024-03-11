from flask import Blueprint, request, jsonify
from ..database import handel as db
from ..database.exceptions import ElementAlreadyExist, ElementDoesNotExist, ElementIsNotEmpty

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/")
def index():
    return "OK"


@api.route('/storages', methods=['POST'])
def create_storage_route():
    data = request.json
    storage = db.create_storage(
        name=data['name'], parent_id=data.get('parent_id', None))
    return jsonify(storage_id=storage.id), 201


@api.route('/storages/<int:storage_id>', methods=['DELETE'])
def delete_storage_route(storage_id):
    try:
        success = db.delete_storage(storage_id=storage_id)
        return jsonify(success=success), 200
    except ElementDoesNotExist as e:
        return jsonify(error=str(e)), 404
    except ElementIsNotEmpty as e:
        return jsonify(error=str(e)), 409


@api.route('/storages/search', methods=['GET'])
def search_storages_route():
    query = request.args.get('query', '')
    storages = db.search_storages(query=query)
    return jsonify(storages=[storage.get_model_dict() for storage in storages]), 200

@api.route('/storages/table', methods=['GET'])
def get_storage_table():
    return jsonify(db.get_all_storages())


@api.route('/items', methods=['POST'])
def create_item_route():
    data = request.json
    try:
        item = db.create_item(
            name=data['name'], description=data['description'], storage_id=data.get('storage_id'))
        return jsonify(item_id=item.id), 201
    except ElementDoesNotExist as e:
        return jsonify(error=str(e)), 404


@api.route('/items/<int:item_id>', methods=['GET'])
def get_item_route(item_id):
    try:
        item = db.get_item_by_id(item_id=item_id)
        return jsonify(name=item.name, description=item.description, storage_id=item.storage_id), 200
    except ElementDoesNotExist as e:
        return jsonify(error=str(e)), 404


@api.route('/items/<int:item_id>', methods=['PUT'])
def edit_item_route(item_id):
    data = request.json
    try:
        item = db.edit_item(item_id=item_id, name=data.get(
            'name'), description=data.get('description'))
        return jsonify(name=item.name, description=item.description, storage_id=item.storage_id), 200
    except ElementDoesNotExist as e:
        return jsonify(error=str(e)), 404


@api.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item_route(item_id):
    try:
        success = db.delete_item(item_id=item_id)
        return jsonify(success=success), 200
    except ElementDoesNotExist as e:
        return jsonify(error=str(e)), 404


@api.route('/items/search', methods=['GET'])
def search_items_route():
    query = request.args.get('query', '')
    items = db.search_items(query=query)
    return jsonify(items=[{'id': item.id, 'name': item.name, 'description': item.description} for item in items]), 200
