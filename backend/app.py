from flask import Flask, jsonify, request
import json
from flask_cors import CORS
import os
from routes import routes_bp

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})


app.register_blueprint(routes_bp)