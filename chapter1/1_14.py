#排序不支持原生比较的对象
import math
from operator import attrgetter
class User:
    def __init__(self,user_id,user_id2):
        self.user_id=user_id
        self.user_id2=user_id2
    def __repr__(self):
        return 'User({},{})'.format(self.user_id,self.user_id2)
def sort_notcompare():
    users=[User(23,999),User(3,99),User(99,9)]
    print(users)
    print(sorted(users,key=lambda u:u.user_id))
    print(sorted(users, key=attrgetter('user_id')))#attrgetter同样适用于max函数
sort_notcompare()








print("{}".format(12313))#占位符{}
print("{1},{0}".format('0','1'))#占位符中标记顺序
print("{name},{message}".format(message='hello',name='girl'))#占位符中使用标签
#< （默认）左对齐
# > 右对齐
# ^ 中间对齐
# = （只用于数字）在小数点后进行补齐
print("{0:10}".format("hello"))
#'b' - 二进制。将数字以2为基数进行输出。
# 'c' - 字符。在打印之前将整数转换成对应的Unicode字符串。
# 'd' - 十进制整数。将数字以10为基数进行输出。
# 'o' - 八进制。将数字以8为基数进行输出。
# 'x' - 十六进制。将数字以16为基数进行输出，9以上的位数用小写字母。
# 'e' - 幂符号。用科学计数法打印数字。用'e'表示幂。
# 'g' - 一般格式。将数值以fixed-point格式输出。当数值特别大的时候，用幂形式打印。
# 'n' - 数字。当值为整数时和'd'相同，值为浮点数时和'g'相同。不同的是它会根据区域设置插入数字分隔符。
# '%' - 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号。

print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))#?
print('The value of PI is approximately {:.3f}.'.format(math.pi))