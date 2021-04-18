# coding:utf-8

from flask import Flask
from setting import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect

import redis
import logging
from logging.handlers import RotatingFileHandler
from flask_demo.utils.common import RegexConverter, MobileConverter


# 数据库
db = SQLAlchemy()

# 创建redis连接对象
redis_store = None

# # 配置日志信息
# # 设置日志的记录等级
# logging.basicConfig(level=logging.INFO)
# # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
# file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# # 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
# formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# # 为刚创建的日志记录器设置日志记录格式
# file_log_handler.setFormatter(formatter)
# # 为全局的日志工具对象（flask app使用的）添加日记录器
# logging.getLogger().addHandler(file_log_handler)


# 工厂模式
def create_app(config_name):
    """
    创建flask的应用对象
    :param config_name: str  配置模式的模式的名字 （"develop",  "product"）
    :return:
    """
    app = Flask(__name__,
                static_url_path='/mystatic', # 访问静态资源的url前缀
                static_folder='static',   # 静态文件的目录，默认就是static
                template_folder='templates'  # 模板文件的目录
                )

    # 根据配置模式的名字获取配置参数的类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 使用app初始化db
    db.init_app(app)

    # 初始化redis工具
    # global redis_store
    # redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # 利用flask-session，将session数据保存到redis中
    # Session(app)

    # 为flask补充csrf防护
    CSRFProtect(app)

    # 为flask添加自定义的转换器
    app.url_map.converters['re'] = RegexConverter
    app.url_map.converters['mobile'] = MobileConverter

    # 注册蓝图
    from flask_demo import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")
    app.register_blueprint(api_1_0.req, url_prefix="/req")
    app.register_blueprint(api_1_0.cok, url_prefix="/cok")
    app.register_blueprint(api_1_0.sql, url_prefix="/sql")

    # 注册提供静态文件的蓝图
    # from ihome import web_html
    # app.register_blueprint(web_html.html)

    # 自定义错误处理信息
    @app.errorhandler(404)
    def handle_404_error(err):
        # 这个函数的返回值是前端用户最终看到的信息
        return '发送错误，详细信息：%s' % err

    return app