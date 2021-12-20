from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from db import setup_db, Foods, get_query, Records
import json
import csv

tag = "Server - "
app = Flask(__name__)
setup_db(app)

CORS(app)

@app.route('/')
def index():
    return "App"

@app.route('/insert')
def troll():
    with open('fooddb.csv', mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            to_add = Foods(int(row['id']), row['name'])
            to_add.insert()
    return "200"

@app.route('/query')
def dispatch_query():
    output = get_query("SELECT {} from foods;".format())
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)