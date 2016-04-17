#读写字节数据
with open('./anotherfile.bin','wb') as f:
    f.write(b'helloworld')
with open('./anotherfile.bin','rb') as f:
    data=f.read()
    print(data)
print(data[0])#索引或迭代返回为字节值
#进行解码操作
text=data.decode('utf-8')
print(text[0])
#写入时需要进行编码操作
text=text.encode('utf-8')
print(text)