#二进制八进制十六进制整数
x=1234
print(bin(x))
print(oct(x))
print(hex(x))
#不输出前缀
print(format(x,'b'))
print(format(x,'o'))
print(format(x,'x'))

#处理负数
x=-1234
print(format(x,'b'))
print(format(x,'x'))
#为了产生无符号值，需进行转换
print(format(2**32+x,'b'))
print(format(2**32+x,'x'))

#其他进制转化为十进制
print(int('4d2',16))
print(int('10011010010',2))

