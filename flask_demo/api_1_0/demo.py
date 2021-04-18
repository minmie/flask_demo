from . import api
from flask_demo import db
from flask_demo import models # 必须要在视图忠导入，否则无法迁移数据库
# import logging
from flask import current_app, request, url_for, redirect, abort, Response,make_response


@api.route('/test')   # http://127.0.0.1:5000/api/v1.0/test
def test():
    return "test ok!"


@api.route('/test2', methods=['POST'])
def test2():
    return 'http post'


@api.route('/test3')
@api.route('/test4')
def test3():
    return "test3 4"


@api.route('/test5')
def test5():   # 函数名字默认就是url名称
    return redirect(url_for('api_1_0.test'))  # 转到/test

@api.route('/student/<int:stu_id>')  # int型转换器
# @api.route('/student/<stu_id>')  # 不加转换器类型，默认是普通字符串，出了/的字符串
def test6(stu_id):
    return 'stu_id %s' % stu_id




@api.route('/email/<re(r"\d+@qq.com"):email>')
def test7(email):
    return 'email: %s' % email


@api.route('/mobile/<mobile:mobile>')
def test8(mobile):
    return 'mobile: %s' % mobile

@api.route('/test9')
def test9():
    return redirect(url_for('api_1_0.test8', mobile="13215946641")) # 会调用mobile转换器的to_url方法



# 上传文件
@api.route('/test10')
def test10():
    # abort立即终止视图函数执行，并返回特定信息给前端
    # 1.必须传递标准状态码
    abort(404)
    # 2. 返回响应体
    # rep = Response("login failed")
    # abort(rep)
    return 'ok'

# 设置响应信息
@api.route('test11')
def test11():
    # 1.使用元素返回自定义响应信息
            # 响应体，状态码，响应头
    # return 'test ok', 201, [('name','arvin'), ('age', 100)]
    # return 'test ok', 201, {'name':'arvin','age':100}  # 两种方式都ok

    # 2.使用make_response
    rep = make_response('test ok')
    rep.status = 201
    rep.headers['name'] = 'arvin'
    rep.headers['age'] = 100
    return rep


# 返回json
@api.route('/test12')
def test12():

    data = {'name':'arvin','age':100}
    rep = make_response(data)
    # 设置cookie
    # rep.set_cookie("name", 'arvin',max_age=60*24) # max_age设置有效期
    # rep.set_cookie('age', "255")

    # 获取cookie
    # print('name=',request.cookies.get("name"))

    # 删除cookie
    # rep.delete_cookie("name")

    return rep


# Flask请求钩子
"""
before_first_request   第一次请求之前
before_request   每次请求前运行
after_request    如果没有未处理的异常，在每次请求后运行
teardown_request  每次请求后运行，即使有未处理的异常
"""

# @current_app.before_first_request
# def handle_before_first_request():
#     print("handle_before_first_request")
#
# @current_app.before_request
# def handle_before_first_request():
#     print("before_request")
#
# @current_app.after_request
# def handle_after_request(response):
#     print("after_request")
#     return response
#
# @current_app.teardown_request
# def handle_teardown_request(response):
#     print("teardown_request")
#     return response

