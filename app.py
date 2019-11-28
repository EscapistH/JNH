from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/check_select_date', methods=['get', 'post'])
def check_select_date():
    if request.method == 'post':
        pass
    else:
        return render_template('index.html')


@app.route('/photo')
def photo():
    return render_template('photo.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
