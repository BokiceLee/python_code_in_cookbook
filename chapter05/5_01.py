#读写文本数据
#全部打出
with open('somefile.txt','rt') as f:
    data=f.read()
print(data)
#迭代每次输出一行
with open('somefile.txt','rt')as f:
    for line in f:
        print(line,end='')

#写入文件，若存在文件则覆盖
with open('somefile.txt','wt') as f:
    f.write("another programmer\nanother programmer")
    print("write this",file=f)
with open('somefile.txt','at') as f:
    print("add ? 你好",file=f)#若文本为二进制模式，打印出错
#一般默认系统编码，可选encoding参数修改
#newline参数设置对换行符的转换 newline=''使\r\n不转化为\n

#with语句块结束自动关闭文件，若非with语句，需手动关闭
f=open('somefile.txt','rt')
data=f.read()
f.close()
#指定编码错误采取方案
#通过errors参数处理编码错误，replace或者ignore
f=open('somefile.txt','rt',encoding='ascii',errors='ignore')
data=f.read()
print(data)