from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from db import setup_db, Foods, get_query, Records
import json

tag = "Server - "
app = Flask(__name__)
setup_db(app)

CORS(app)

@app.route('/')
def index():
    return "App"

@app.route('/troll')
def troll():
    food = Foods("음식맨",5)
    food.insert()
    return food.format()

@app.route('/query')
def dispatch_query():
    output = get_query("SELECT * from foods;")
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)