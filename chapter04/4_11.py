#同时迭代多个序列(不止两个
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99,12]
for x, y in zip(xpts, ypts):
    print(x,y)
#迭代长度与短序列长度相同
from itertools import zip_longest
for a,b in zip_longest(xpts,ypts,fillvalue=0):
    print(a,b)
print(dict(zip_longest(xpts,ypts,fillvalue=0)))#可转化为字典或列表