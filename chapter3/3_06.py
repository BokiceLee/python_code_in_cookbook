import cmath
import numpy
#复数的数学运算
#使用complex函数表示
a=complex(2,4)
#用后缀j
b=3-5j
print(a)
print(b)

#获取实部、虚部、共轭复数
print(a.real)
print(a.imag)
print(a.conjugate())
#支持加减乘除运算
print(a+b)

#通过cmath模块支持复数函数
print(cmath.sin(a))#正弦
print(cmath.cos(a))#余弦
print(cmath.exp(a))#e的a次

#使用numpy模块
a=numpy.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a+2)
print(numpy.sin(a))

print(cmath.sqrt(-1))