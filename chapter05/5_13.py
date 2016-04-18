#获取文件夹中的文件列表
import os
import time
names=os.listdir('.')
print(names)

#进行文件名的匹配
import glob
pyfiles=glob.glob('.\*.py')
print(pyfiles)
for file in pyfiles:
    print(file,os.path.getsize(file),time.ctime(os.path.getmtime(file)))
#或者
from fnmatch import fnmatch
pyfiles=[name for name in os.listdir('.') if fnmatch(name,'*.py')]
print(pyfiles)
for file in pyfiles:
    print(file,os.stat(file).st_size,os.stat(file).st_mtime)