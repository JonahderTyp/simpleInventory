from flask import Blueprint, request, jsonify
from database import handel as db

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/")
def index():
    return "OK"

@api.route('/storage', methods=['POST'])
def create_storage_route():
    data = request.json
    storage = db.create_storage(data['name'], data.get('parent_id'))
    return jsonify({'id': storage.id, 'name': storage.name, 'parent_id': storage.parent_id}), 201

@api.route('/storage/<int:storage_id>', methods=['DELETE'])
def delete_storage_route(storage_id):
    if db.delete_storage(storage_id):
        return jsonify({'message': 'Storage deleted'}), 200
    else:
        return jsonify({'message': 'Deletion failed'}), 400

@api.route('/storage/<int:storage_id>/items', methods=['GET'])
def get_items_route(storage_id):
    items_with_paths = db.get_items_with_paths(storage_id)
    return jsonify(items_with_paths), 200

@api.route('/item', methods=['POST'])
def create_item_route():
    data = request.json
    item = db.create_item(data['name'], data['description'], data['storage_id'])
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description, 'storage_id': item.storage_id}), 201

@api.route('/item/<int:item_id>', methods=['DELETE'])
def delete_item_route(item_id):
    if db.delete_item(item_id):
        return jsonify({'message': 'Item deleted'}), 200
    else:
        return jsonify({'message': 'Deletion failed'}), 400

@api.route('/item/<int:item_id>', methods=['PUT'])
def edit_item_route(item_id):
    data = request.json
    item = db.edit_item(item_id, data.get('name'), data.get('description'))
    if item:
        return jsonify({'id': item.id, 'name': item.name, 'description': item.description}), 200
    else:
        return jsonify({'message': 'Update failed'}), 400
