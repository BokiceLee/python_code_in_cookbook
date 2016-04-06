#排序列表
rows = [ {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
         {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
         {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
         {'fname': 'Big', 'lname': 'Jones', 'uid': 1004} ]
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
rows_by_fname_lname=sorted(rows,key=itemgetter('fname','lname'))
print(rows_by_fname_lname)#支持多个字段排序

#同样适用于max、min
print(max(rows,key=itemgetter('uid')))

#可以用lambda表达式代替
rows_sorted_by_udi=sorted(rows,key=lambda k:(k['fname'],k['lname']))
print(rows_sorted_by_udi)