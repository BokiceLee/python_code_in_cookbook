#读写压缩文件
import gzip
#bz2同
with gzip.open('somefile.gz','rt') as f:
    data=f.read()
    print(data)
#其他操作同普通文件