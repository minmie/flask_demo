from . import cok
from flask import request, make_response,session


@cok.route('/test1')
def test1():
    data = {'name': 'arvin', 'age': 100}
    rep = make_response(data)
    # 设置cookie
    rep.set_cookie("name", 'arvin',max_age=60*24) # max_age设置有效期
    rep.set_cookie('age', "255")

    # 获取cookie
    print('name=',request.cookies.get("name"))

    # 删除cookie
    rep.delete_cookie("name")
    return rep


@cok.route('/test2')
def test2():
    # 设置session
    session['name'] = 'arvin'
    session['age'] = '28'
    return 'success'

@cok.route('/test3')
def test3():
    # 获取session
    name=session.get('name')
    return 'name=%s' % name