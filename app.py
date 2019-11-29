from flask import *
# from flask_sqlalchemy import SQLAlchemy

from controller.photo import photo
from controller.article import article
from controller.index import index

app = Flask(__name__)
app.register_blueprint(photo, url_prefix='/photo')
app.register_blueprint(article, url_prefix='/article')
app.register_blueprint(index, url_prefix='/')
app.register_blueprint(index, url_prefix='/index')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# # 连接数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/jnh'
#
# # 设为 False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# # 显示原始sql语句
# app.config['SQLALCHEMY_ECHO'] = True
# db = SQLAlchemy(app)
#
#
# class Article(db.Model):
#     # 表名
#     __tablename__ = 'article'
#     # 列名
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(64))
#     content = db.Column(db.Text)
#
#     def __repr__(self):
#         return 'article title: {}\n content: {}'.format(self.title, self.content)


if __name__ == '__main__':
    app.run()
