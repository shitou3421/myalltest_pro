# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/27 15:26
from collections import deque

q = deque(maxlen=5)

q.append(1)
print(q)
q.append(2)
print(q)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)
q.append(6)
print(q)
a = q.pop()
print(q)
print(a)
b= q.popleft()
print(q)
print(b)

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open("02_deque_test.txt") as f:
        for line, prevlines in search(f, "python", 5):
            for pline in prevlines:
                print(pline, end="")
            print(line, end="")
            print("-"*20)



