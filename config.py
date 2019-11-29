class Config(object):
    # 设置数据库地址
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/jnh'
    # 追踪更新，设置False以压制waring
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 设置 SECRET_KEY
    SECRET_KEY = 'sk'

