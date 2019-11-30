from flask import render_template, Blueprint

error = Blueprint('error', __name__)


@error.app_errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404


@error.app_errorhandler(500)
def handle_500(e):
    # TODO: 编写一个500.html来响应这个错误页面
    # return render_template('500.html'), 500
    return render_template('404.html'), 500
