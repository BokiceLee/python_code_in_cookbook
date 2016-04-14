#反向迭代
a=[1,2,3,4,5]
for x in reversed(a):
    print(x)

#反向迭代条件
#1、对象大小预先可知
#2、对象实现了__reverse__方法

#自定义类实现__reverse__方法
class Countdown :
    def __init__(self, start):
        self.start = start
# Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
# Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
for rr in reversed(Countdown(30)):
    print(rr)
for rr in Countdown(30):
    print(rr)
