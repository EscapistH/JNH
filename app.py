from flask import Flask, render_template

# 导入配置
from config import Config

# 初始化程序并导入配置
app = Flask(__name__)
app.config.from_object(Config)

# 导入flask_sqlalchemy模块 并初始化db对象
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# 导入controller并注册url
from controller.index import index
from controller.article import article
from controller.photo import photo

# 注册蓝图url
app.register_blueprint(index, url_prefix='/')
app.register_blueprint(index, url_prefix='/index')
app.register_blueprint(photo, url_prefix='/photo')
app.register_blueprint(article, url_prefix='/article')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    # 程序启动入口
    app.run()
