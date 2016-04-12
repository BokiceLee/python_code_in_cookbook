#数字的格式化输出
x=113423.5231
print(format(x,'0.2f'))
print(format(x,'>10.1f'))
print(format(x,'<10.1f'))
print(format(x,','))
print(format(x,'0,.1f'))
print(format(x,'e'))#使用指数记法e/E
#一般形式是 '[<>ˆ]?width[,]?(.digits)?' ，其中 width 和 digits 为整数，？代表可选部分
#decimal模块也支持以上操作