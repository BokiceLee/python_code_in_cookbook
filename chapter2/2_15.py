#字符串中插入变量
import sys
s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))
name = 'Guido'
#n = 37
#print(s.format_map(vars()))#使用vars()获得变量

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
a = Info('Guido',37)
print(vars(a))
print(s.format_map(vars(a)))#var()适用于对象实例

#以上两种方法均不能处理变量缺失，处理方法为定义一个含有 missing () 方法的字典对象
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'
print(safesub(vars()))
print(s.format_map(safesub(vars())))



#封装插入函数
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
#使用 sys. getframe(1) 返回调用者的栈帧。访问属性 f locals 来获得局部变量。
print(sub('Hello {name}'))