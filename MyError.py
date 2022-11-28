# # 自定义异常类 MyError ，继承普通异常基类 Exception
# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return repr(self.value)

# 括号异常类
class brackets_error(Exception):
    def __init__(self, value):
        self.value = value
