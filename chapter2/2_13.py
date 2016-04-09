#字符串对齐
text='Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
#可接受一个填充字符
print(text.center(20,'*'))
print(format(text,'*^20'))#用format实现同样效果
print('{:>10} {:>10}'.format('Hello','World'))#格式化多个值

x=1.2345
print(format(x,'>10'))
print(format(x,'^10.2f'))#format可以格式任意类型的值