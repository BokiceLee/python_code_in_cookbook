#find the nlargest elements
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
#num=heapq.heapify(nums)
print(nums)
print(sorted(nums)[-3:])
for i in range(0,3):
    n=heapq.heappop(nums)
    print(n)

#heap sort
portfolio = [ {'name': 'IBM', 'shares': 100, 'price': 91.1},
              {'name': 'AAPL', 'shares': 50, 'price': 543.22},
              {'name': 'FB', 'shares': 200, 'price': 21.09},
              {'name': 'HPQ', 'shares': 35, 'price': 31.75},
              {'name': 'YHOO', 'shares': 45, 'price': 16.35},
              {'name': 'ACME', 'shares': 75, 'price': 115.65} ]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])#how about lambda
print((list(map(lambda s:s['price'],cheap))))# about map in python3
print(expensive)
