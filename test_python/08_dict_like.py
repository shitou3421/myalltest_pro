# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/27 16:45



a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(b.keys() - a.keys())
print(a.items() & b.items())
print(a.items() - b.items())
print(b.items() - a.items())
