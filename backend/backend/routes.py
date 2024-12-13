
from flask import Blueprint, jsonify
import json
from flask_cors import CORS
import os

routes_bp = Blueprint('routes', __name__)

DATA_PATH = 'data/searches.json'

@routes_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Hello"})

def load_data():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, 'r') as f:
        return json.load(f)

@routes_bp.route('/searches', methods=['GET'])
def get_searches():
    data = load_data()   
    return jsonify({ 
        'data': data 
    })


@routes_bp.route('/searches/all', methods=['GET'])
def get_all():
    data = load_data()
    return jsonify(data)


@routes_bp.route('/searches', methods=['POST'])
def create():
    return jsonify({'error': 'Method not implemented'}), 501

@routes_bp.route('/searches/<int:id>', methods=['PUT'])
def update(id):
    return jsonify({'error': 'Method not implemented'}), 501

@routes_bp.route('/searches/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify({'error': 'Method not implemented'}), 501