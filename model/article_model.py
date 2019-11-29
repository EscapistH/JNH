from flask_sqlalchemy import SQLAlchemy
from app import app

# 连接数据库的url
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/jnh'

# 设为 False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 显示原始sql语句
db = SQLAlchemy(app)


class Article(db.Model):
    # 表名
    __tablename__ = 'article'
    # 列名
    article_id = db.Column(db.Integer, primary_key=True)
    article_title = db.Column(db.String(64))
    article_auth = db.Column(db.String(64))
    article_content = db.Column(db.Text)

    def __repr__(self):
        return 'article: 《{}》\nby{}\ncontent: {}'.format(self.article_title, self.article_auth, self.article_content)
