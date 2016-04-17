#字符串的IO操作 ？ 模拟普通文件？
import io
#文本
s=io.StringIO()
s.write('Hello')
print('world',file=s)
print(s.getvalue())
anothers=io.StringIO('aaaaa')
print(anothers.read(3))
print(anothers.read())
#二进制数据使用BytesIO()