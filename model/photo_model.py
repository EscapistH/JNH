from flask_sqlalchemy import SQLAlchemy
from app import app

# 连接数据库的url
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/jnh'
#
# # 设为 False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 显示原始sql语句
db = SQLAlchemy(app)


class Article(db.Model):
    # 表名
    __tablename__ = 'photo'
    # 列名
    photo_id = db.Column(db.Integer, primary_key=True)
    photo_title = db.Column(db.String(64))
    photo_path = db.Column(db.String(64))

    def __repr__(self):
        return 'photo name: {}\n at {}'.format(self.photo_title, self.photo_path)
