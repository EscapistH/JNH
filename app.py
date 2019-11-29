from flask import *
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


if __name__ == '__main__':
    print(url_for('index'))
    app.run()
