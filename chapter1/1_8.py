prices = { 'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }
min_price = min(zip(prices.values(), prices.keys()))# zip() 函数创建的是一个只能访问一次的迭 代器
# min_price is (10.75, 'FB')
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(list(prices_sorted))
min(prices, key=lambda k: prices[k])
# Returns 'FB'
max(prices, key=lambda k: prices[k])
# Returns 'AAPL'
