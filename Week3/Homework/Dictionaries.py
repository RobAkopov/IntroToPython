market = {'dairy': ['yogurt', 'cheese'], 'fruits': ['banana', 'apple', 'orange', 'lemon', 'apple', 'banana','banana']}
print(market)
market.update({'candies' : ['mars', 'kinder', 'twix']})
print(market)
market["fruits"] = sorted(list(set(market["fruits"])))
print(market)