#字节到大整数的打包和解包
data=b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(int.from_bytes(data,'little'))#小端次数
print(int.from_bytes(data,'big'))
x= 94522842520747284487117727783387188
print(x.bit_length()/8)
nbytes,rem=divmod(x.bit_length(),8)
if rem:
    nbytes+=1
print(nbytes,rem)#字节数的多少
print(x.to_bytes(nbytes,'big'))
print(x.to_bytes(16,'big'))
print(x.to_bytes(nbytes,'little'))
