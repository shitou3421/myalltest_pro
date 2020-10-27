# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/27 16:29

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'IBMa': 205.551,
    'IBM2': 205.551,
    'HPQ': 37.20,
    'FB2': 10.75,
    'FB1': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
ma_price = max(zip(prices.keys(), prices.values())) # 根据字符排序

price_sort = sorted(zip(prices.values(), prices.keys()), reverse=True)

print(min_price, max_price, ma_price)
print(price_sort)

print(min(prices.values()))
print(max(prices.values()))

print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))

print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))


