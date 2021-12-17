from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.dialects.postgresql import ARRAY
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json

from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey

tag = "DB - "
db_name = "fooddb"
db_user = "postgres"
db_pass = "!postgre!2"
db_url = "localhost"
db_port = "5432"

db_path = "postgresql://{}/{}".format(
    db_user + ":" + db_pass + "@" + db_url+ ":" + db_port, db_name
    )

db = SQLAlchemy()

def setup_db(app, db_path=db_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    print(tag+"Setup Completed.")

def get_query(q):
        raw_output = db.session.execute(q).fetchall()
        output = []
        for r in raw_output:
            data = jsonify(id=r['id'], name=r['name'], taste=r['taste'])
            output.append(data.get_json())
        return output

class Foods(db.Model):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True, nullable=False)
    taste = Column(Integer, nullable=False)
    
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            print(tag+"Cannot insert data.")

    def update(self):
        db.session.commit()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            print(tag+"Cannot delete data.")
    
    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "taste": self.taste
        }


class Records(db.Model):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    before = Column(String(64), nullable=False)
    now = Column(String(64), nullable=False)
    
    def __init__(self, id, before, now):
        self.id = id
        self.before = before
        self.now = now

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def format(self):
        return {
            "id": self.id,
            "before": self.before,
            "now": self.now
        }