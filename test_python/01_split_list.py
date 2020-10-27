# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/27 15:08


def desc_num(list):
    a, b, c, _ = list
    return a, b, c


def desc_num1(list):
    a, *b, c = list
    return b


def do_foo(x, y):
    print("foo", x, y)

def do_bar(s):
    print("foo", s)

def desc_num2(obj):
    for tag, *args in obj:
        if tag == "foo":
            do_foo(*args)
        elif tag == "bar":
            do_bar(*args)

if __name__ == '__main__':
    print(desc_num([1, 2, 3, 4]))
    print(desc_num1([1, 2, 3, 4, 5, 6, 7, 8]))
    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
    ]
    desc_num2(records)

