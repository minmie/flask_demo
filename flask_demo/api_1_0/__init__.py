# coding:utf-8

from flask import Blueprint


# 创建蓝图对象
# 第一个参数：蓝图的名字，可用于反向解析
api = Blueprint("api_1_0", __name__)
req = Blueprint('request',__name__)
cok = Blueprint('cookie',__name__)
sql = Blueprint('sql',__name__)


# 导入蓝图的视图
from . import demo,request_demo,cookie_,sql_
