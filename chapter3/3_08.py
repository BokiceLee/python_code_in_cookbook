#分数运算
from fractions import Fraction
#fractions模块用来执行包含分数的数学计算
a=Fraction(5,4)
b=Fraction(7,16)
print(a+b)
print(a*b)
print(a.numerator)#分子
print(a.denominator)#坟墓
print(float(a))
#通过限制分母获得一个被覆盖的分数
print(b.limit_denominator(16))
#小数转化为分数
x=3.75
print(x.as_integer_ratio())
y=Fraction(*x.as_integer_ratio())
print(y)