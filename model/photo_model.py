from app import db


class Photo(db.Model):
    # 表名
    __tablename__ = 'photo'
    # 列名
    photo_id = db.Column(db.Integer, primary_key=True)
    photo_title = db.Column(db.String(64))
    photo_path = db.Column(db.String(64))

    def __repr__(self):
        return 'photo: {} at {}'.format(self.photo_title, self.photo_path)
