# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/27 16:16
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(2)
d['b'].append(3)

print(d)
print(d.get('a'))
print(d.get('b'))

b = defaultdict(set)
b['a'].add(1)
b['a'].add(2)
b['a'].add(2)
b['b'].add(3)

print(b)
print(b.get('a'))
print(b.get('b'))

c = defaultdict(dict)
c['a'].update({"a":"1"})
c['b'].update({"a":"2"})
c['c'].update({"a":"3"})
c['d'].update({"b":"4"})


print(c)
print(c.get('a'))
print(c.get('b'))







