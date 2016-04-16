#不同集合上元素的迭代
from itertools import chain
a=[1,2,3,4]
b=['x','b']
for x in chain(a,b):
    print(x)
#支持不同类型集合不同类型元素