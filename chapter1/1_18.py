#映射名称到序列元素
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])#typename
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        #print(*rec)    *号可将数据从元组中提取出来
        s = Stock(*rec)
    total += s.shares * s.price
    return total
print(compute_cost([(1,2,3)]))


#可用于替换字典，但是值的修改需要使用replace函数
s = Stock('ACME', 100, 123.45)
s=s._replace(price=90)
print(s.price)
print(s)

#填充数据,包含默认值
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))