from flask import *

# 导入controller
from controller.index import index
from controller.article import article
from controller.photo import photo

# 导入model
from model.article_model import Article
from model.photo_model import Photo

# 导入配置
from config import Config

app = Flask(__name__)
app.config.from_pyfile(Config)
app.register_blueprint(index, url_prefix='/')
app.register_blueprint(index, url_prefix='/index')
app.register_blueprint(photo, url_prefix='/photo')
app.register_blueprint(article, url_prefix='/article')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
