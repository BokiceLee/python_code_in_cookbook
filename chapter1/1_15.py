#通过字段将记录分组
from operator import itemgetter
from itertools import groupby
from collections import defaultdict
rows = [ {'address': '5412 N CLARK', 'date': '07/01/2012'},
         {'address': '5148 N CLARK', 'date': '07/04/2012'},
         {'address': '5800 E 58TH', 'date': '07/02/2012'},
         {'address': '2122 N CLARK', 'date': '07/03/2012'},
         {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
         {'address': '1060 W ADDISON', 'date': '07/02/2012'},
         {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
         {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
         ]
rows.sort(key=itemgetter('date'))
for date,items in groupby(rows,key=itemgetter('date')):#groupby 查找值连续相同的项
    print(date,list(items))
    #for i in items:
    #    print(' ',i)

rows_by_date=defaultdict(list)#使用defaultdict，将分组结果直接放置到更大的数据中去
for row in rows:
    rows_by_date[row['date']].append(row)
print(dict(rows_by_date))