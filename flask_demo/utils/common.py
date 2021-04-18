from werkzeug.routing import BaseConverter

# 1. 自定义转换器
class RegexConverter(BaseConverter):

    def __init__(self, url_amp, regex):  # 第一个参数固定url_amp，第二个参数是r"\d+@qq.com"
        super().__init__(url_amp)
        self.regex = regex


class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super().__init__(url_map)
        self.regex = r'1[34578]\d{9}'

    def to_python(self, value):  # 视图函数最终接收的参数是这个函数的返回值
        return value

    def to_url(self, value):   # 反向解析的时候会调用这个方法
        return value