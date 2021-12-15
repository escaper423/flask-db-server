from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from db import setup_db, Foods, Records

app = Flask(__name__)
setup_db(app)

CORS(app)

@app.route('/')
def index():
    return "App"

@app.route('/troll')
def troll():
    return jsonify({
        "id": 1,
        "name": "Pizza",
    })

if __name__ == "__main__":
    app.run(debug=True)