from db import db
# from flask_login import UserMixin
# from sqlalchemy import ForeignKey
# from sqlalchem.sql import func


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(50), nullable=True)
    reason = db.Column(db.String(80),default=3) # 1=admin,2=developer, 3=guest
    address = db.Column(db.String(80), nullable=False)