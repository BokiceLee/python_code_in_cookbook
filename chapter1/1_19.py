import os
files=os.listdir('./')
if any(name.endswith('.py') for name in files):#endswith 匹配后缀
    print("There are python files")
else:
    print("There is no python file")

s = ('ACME', 50, 123.45)
print('，'.join(str(x) for x in s))# 连接
# Data reduction across fields of a data structure
portfolio = [ {'name':'GOOG', 'shares': 50},
              {'name':'YHOO', 'shares': 75},
              {'name':'AOL', 'shares': 20},
              {'name':'SCOX', 'shares': 65} ]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)