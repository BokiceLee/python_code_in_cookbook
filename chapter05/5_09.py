#读取二进制数据到可变缓冲区中
import os.path
def read_into_buffer(filename):
    buf=bytearray(os.path.getsize(filename))
    with open(filename,'rb') as f:
        f.readinto(buf)
    return buf
buf=read_into_buffer('anotherfile.bin')
print(buf)