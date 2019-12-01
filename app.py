from flask import Flask

# 导入配置
from config import Config

# 初始化程序并导入配置
app = Flask(__name__)
app.config.from_object(Config)

# 导入flask_sqlalchemy模块 并初始化db对象
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# 导入views并注册url
from jnh.views import *

# 注册视图 url
app.register_blueprint(error)
app.register_blueprint(index, url_prefix='/')
app.register_blueprint(index, url_prefix='/index')
app.register_blueprint(photo, url_prefix='/photos')
app.register_blueprint(article, url_prefix='/articles')


if __name__ == '__main__':
    # 程序启动入口
    app.run()
