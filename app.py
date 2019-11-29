from flask import *
from controller.photo import photo
from controller.article import article

app = Flask(__name__)
app.register_blueprint(photo, url_prefix='/photo')
app.register_blueprint(article, url_prefix='/article')


# TODO：把主页面也重写成Controller 以app.register_blueprint注册到app中

@app.route('/')
def redirect_to_index():
    return redirect('index')


@app.route('/index')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
