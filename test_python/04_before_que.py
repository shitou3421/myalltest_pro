# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/27 15:59
import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1] # 返回item对象

class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({})'.format(self.name)

q = PriorityQueue()

q.push(Item('foo'), 1)
q.push(Item('bar'), 2)
q.push(Item('spam'), 5)
q.push(Item('dog'), 4)
q.push(Item('fish'), 8)
q.push(Item('fish'), 4)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())










