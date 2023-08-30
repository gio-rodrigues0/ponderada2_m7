from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user = db.Column(db.String(100), nullable=False)
        password = db.Column(db.String(300), nullable=False)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)

def createTables(app):

    with app.app_context():
        db.create_all()

def main():
    createTables()

if __name__ == "__main__":
    main()