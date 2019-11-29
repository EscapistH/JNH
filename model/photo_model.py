from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


class Photo(db.Model):
    # 表名
    __tablename__ = 'photo'
    # 列名
    photo_id = db.Column(db.Integer, primary_key=True)
    photo_title = db.Column(db.String(64))
    photo_path = db.Column(db.String(64))

