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


class Photo(db.Model):
    # 表名
    __tablename__ = 'photo'
    # 列名
    photo_id = db.Column(db.Integer, primary_key=True)
    photo_title = db.Column(db.String(64))
    photo_path = db.Column(db.String(64))

    def __repr__(self):
        return 'photo: {} at {}'.format(self.photo_title, self.photo_path)
