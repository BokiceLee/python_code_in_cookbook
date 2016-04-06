from collections import defaultdict
d=defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)
#另一种做法
d = {} # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)
#做法对比
#一般做法
d = {}
#for key, value in pairs:
 #   if key not in d:
#        d[key] = []
#    d[key].append(value)
#defaultdict
#d = defaultdict(list)
#for key, value in pairs:
#    d[key].append(value)