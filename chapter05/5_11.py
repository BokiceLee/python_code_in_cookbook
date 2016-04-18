#文件路径名的操作
import os
path='./somefile.txt'
print(os.path.basename(path))

print(os.path.dirname(path))

path='-/somefile.txt'
print(os.path.expanduser(path))#???????????
print(os.path.splitext(path))