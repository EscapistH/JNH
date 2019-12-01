class Config(object):
    # 设置数据库地址
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/jnh'
    # 关闭数据追踪，设置False以压制waring
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 开启自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 设置 SECRET_KEY
    SECRET_KEY = 'sk'

