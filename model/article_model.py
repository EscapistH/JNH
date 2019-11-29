from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


class Article(db.Model):
    # 表名
    __tablename__ = 'article'
    # 列名
    article_id = db.Column(db.Integer, primary_key=True)
    article_title = db.Column(db.String(64))
    article_auth = db.Column(db.String(64))
    article_content = db.Column(db.Text)
