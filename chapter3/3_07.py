#无穷大与NaN
import math
a=float('inf')
print(a)

b=float('-inf')
print(b)

c=float('nan')
print(c)
print(math.isinf(a))
print(math.isnan(c))

#无穷大进行数学计算的传播
print(a+45,1000/b)

#返回Nan结果
print(a/a)
print(a+b)

#NaM在计算中传播
print(c+1111)
print(c**2)

#NaN的比较操作总是返回False
d=float('nan')
print(c==d)
print(c==c)