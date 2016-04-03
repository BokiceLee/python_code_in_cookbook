from collections import OrderedDict
import json
def ordered_dict():
    d = OrderedDict()
    d['foo'] = True
    d['bar'] = (1,2)
    d['spam'] = 6
    d['grok'] = 4 # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
    print(d)
    d=json.dumps(d)#转化为json编码，此处用于说明ordereddict的作用
    print(d)
   # for key in d:
   #     print(key, d[key])
ordered_dict()
