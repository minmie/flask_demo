from flask import Flask, abort



app =Flask(__name__)



@app.route('/hello')
def hell():
    abort(404)
    return 'hello flask'


# 自定义错误处理信息
@app.errorhandler(404)
def handle_404_error(err):
    # 这个函数的返回值是前端用户最终看到的信息
    return '发送错误，详细信息：%s'% err

if __name__ == '__main__':
    app.run(port=5001)