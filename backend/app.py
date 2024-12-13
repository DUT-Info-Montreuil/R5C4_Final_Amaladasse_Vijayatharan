from flask import Flask, jsonify, request
import json
from flask_cors import CORS
import os


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})


DATA_PATH = 'data/searches.json'

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Hello"})

def load_data():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, 'r') as f:
        return json.load(f)

@app.route('/searches', methods=['GET'])
def get_searches():
    data = load_data()   
    return jsonify({ 
        'data': data 
    })


@app.route('/searches/all', methods=['GET'])
def get_all():
    data = load_data()
    return jsonify(data)


@app.route('/searches', methods=['POST'])
def create():
    return jsonify({'error': 'Method not implemented'}), 501

@app.route('/searches/<int:id>', methods=['PUT'])
def update(id):
    return jsonify({'error': 'Method not implemented'}), 501

@app.route('/searches/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify({'error': 'Method not implemented'}), 501

