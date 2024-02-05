#!/usr/bin/python3
"""State view"""
from api.v1.views import app_views
from models.state import State
from models import storage
from flask import jsonify, abort, make_response, request


@app_views.route('/states', methods=['GET'])
def all_states():
    """Retrieves the list of all State objects"""
    all_states = []
    for obj in storage.all('State').values():
        all_states.append(obj.to_dict())
    return jsonify(all_states)


@app_views.route('/states/<string:state_id>', methods=['GET'])
def state_id(state_id):
    """Retrieves a State object by it's id"""
    state_obj = storage.get("State", state_id)
    if not state_obj:
        abort(404)
    return jsonify(state_obj.to_dict())


@app_views.route('/states/<string:state_id>', methods=['DELETE'])
def del_state(state_id):
    """Deletes a State object by it's id"""
    state_obj = storage.get("State", state_id)
    if not state_obj:
        abort(404)
    state_obj.delete()
    state_obj.save()
    return jsonify({})


@app_views.route('/states/', methods=['POST'])
def create_state():
    """Creates a State using HTTP POST method"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    state_obj = State(**request.get_json())
    state_obj.save()
    return make_response(jsonify(state_obj.to_dict()), 201)


@app_views.route('/states/<string:state_id>', methods=['PUT'])
def put_state():
    """Updates a State object using HTTP PUT method"""
    state_obj = storage.get("State", state_id)
    if not state_obj:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attrib, value in request.get_json().items():
        if attrib not in ['id', 'created_at', 'updated_at']:
            setattr(state_obj, attrib, value)
    state_obj.save()
    return jsonify(state_obj.to_dict())
