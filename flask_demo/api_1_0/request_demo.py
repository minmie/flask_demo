from . import req
from flask import request

@req.route('/test1')
def test1():
    # 提取表单数据
    name = request.form.get('name')
    age = request.form.get('age')

    # 提取查询字符串数据
    city = request.args.get("city")
    return {'name':name, 'age':15}

@req.route('/test2')
def test2():
    file_obj = request.files.get('pic')
    if not file_obj:
        return '未上传'

    file_obj.save('./demo.png')
    return '上传成功'