# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/27 15:38
import heapq


def search(list):
    min_list = heapq.nsmallest(3, list)
    max_list = heapq.nlargest(3, list)
    return min_list, max_list

def search1(list):
    min_list = heapq.nsmallest(2, list, key=lambda s:s["price"])
    max_list = heapq.nlargest(2, list, key=lambda s:s["price"])
    return min_list, max_list


if __name__ == '__main__':
    print(search([1, 2, 3, 43, 4, 5, 55, 6, 7, 8, 89, 9, 9, 1000]))
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(search1(portfolio))

    my_list = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    aaa = list(my_list)
    heapq.heapify(aaa) # 堆化排序，0号元素永远是最小的
    print(aaa)
    a = heapq.heappop(aaa)
    print(a)
    print(aaa)
    ab= heapq.heappop(aaa)
    print(ab)
    print(aaa)
    ab= heapq.heappop(aaa)
    print(ab)
    print(aaa)
