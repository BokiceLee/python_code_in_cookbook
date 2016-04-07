#使用shell通配符匹配字符串
from fnmatch import fnmatch,fnmatchcase
print(fnmatch('foo.txt','*.txt'))
print(fnmatch('foo.txt','?oo.txt'))
print(fnmatch('Dat45.csv','Dat[0-9]*'))

names= ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
re=[name for name in names if fnmatch(name,'Dat*.csv')]
print(re)

#大小写敏感规则视不同系统而定
re=[name for name in names if fnmatch(name,'dat*.csv')]
print(re)#win下不敏感
#用fnmatchcase完全匹配大小
re=[name for name in names if fnmatchcase(name,'dat*.csv')]
print(re)

#也可以进行列表推导
addresses = [ '5412 N CLARK ST',
              '1060 W ADDISON ST',
              '1039 W GRANVILLE AVE',
              '2122 N CLARK ST',
              '4802 N BROADWAY', ]
ans=[addr for addr in addresses if fnmatchcase(addr ,'* ST')]
print(ans)

ans=[addr for addr in addresses if fnmatchcase(addr ,'54[0-9][0-9] *CLARK*')]
print(ans)