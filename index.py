from flask import Flask, jsonify, request
from flask.helpers import make_response
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
    output = get_query("SELECT * from foods;")
    return jsonify(output)

@app.route('/record', methods=['GET','POST'])
def add_record():
    if request.method == 'POST':
        print(tag+"Adding Record...")
        bf = request.args.get('before','')
        now = request.args.get('now','')
        print("bf: {}, now: {}".format(bf,now))

        to_add = Records(bf,now)
        to_add.insert()
        response = app.response_class(status=200)
        return response
    else:
        print(tag+"Getting Record...")
        return app.response_class(status=200)

    
@app.errorhandler(404)
def not_found(err):
    return "1"



if __name__ == "__main__":
    app.run(debug=True)