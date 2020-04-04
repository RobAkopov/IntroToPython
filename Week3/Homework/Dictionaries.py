market = {'dairy': ['yogurt', 'cheese'], 'fruits': ['banana', 'apple', 'orange', 'lemon', 'apple', 'banana','banana']}
print(market)
market.update({'candies' : ['mars', 'kinder', 'twix']})
print(market)
a = market['fruits']
b = set(a)
c = list(b)
c.sort()
print(c)