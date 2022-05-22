from app import db
from datetime import datetime

class User(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable= False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0) # -1 banned 0 needs email verification 1 ok
    register_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)