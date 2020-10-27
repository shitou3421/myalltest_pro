# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/27 16:25
import json
from collections import OrderedDict

d = OrderedDict()  # 内存消耗将会比普通的大两倍
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

print(json.dumps(d))



