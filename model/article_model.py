from app import db


class Article(db.Model):
    # 表名
    __tablename__ = 'article'
    # 列名
    article_id = db.Column(db.Integer, primary_key=True)
    article_title = db.Column(db.String(64))
    article_auth = db.Column(db.String(64))
    article_content = db.Column(db.Text)

    def __repr__(self):
        return '《{}》\n\t-- by {}\n{}'.format(self.article_title, self.article_auth, self.article_content)
