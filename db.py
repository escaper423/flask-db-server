from sqlalchemy import Column, String, Integer, create_engine, exc
from sqlalchemy.dialects.postgresql import ARRAY
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from bs4 import BeautifulSoup
import requests
import json
import requests
import os

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

class Foods(db.Model):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True )
    name = Column(String(64), unique=True, nullable=False)
    image_url = Column(String(256), unique=True, nullable=True)
    
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def insert(self):
        try:
            url = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiX8JqToIL1AhVGeXAKHdz8CgkQ_AUoAnoECAMQBA&biw=1920&bih=937&dpr=1".format(self.name)
            r = requests.get(url)
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            links = soup.find_all('img', src=True, limit=2)
            self.image_url = links[1].get('src')

            db.session.add(self)
            db.session.commit()
        except exc.SQLAlchemyError as e: 
            print(tag+"Cannot insert data."+str(e))

    def update(self):
        db.session.commit()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except exc.SQLAlchemyError as e: 
            print(tag+"Cannot delete data."+str(e))

    def get_query(q):
        raw_output = db.session.execute(q).fetchall()
        output = []
        for r in raw_output:
            data = jsonify(id=r['id'], name=r['name'])
            output.append(data.get_json())
        return output

    def get_url(q):
        result = db.session.execute(q).fetchone()
        print(result)
        return result['image_url']

        

    

class Records(db.Model):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    before = Column(String(64), nullable=False)
    now = Column(String(64), nullable=False)
    
    def __init__(self, before, now):
        self.before = before
        self.now = now

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except exc.SQLAlchemyError as e: 
            print(tag+"Cannot insert data."+str(e))

    def update(self):
        db.session.commit()

    def get_query(q):
        raw_output = db.session.execute(q).fetchall()
        output = []
        for r in raw_output:
            data = jsonify(name=r['now'], count=r['count'])
            output.append(data.get_json())
        return output

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except exc.SQLAlchemyError as e: 
            print(tag+"Cannot insert data."+e)
        