list2 = ['a', 1, 'b', 2, 'c', 3]
y = int(input('Write a number: '))
z = input('Write letters: ')
list2.append(y)
list2.append(z)
print('list2:', list2)
print('count of numbers', y, ':', list2.count(y))
print('count of letters', z, ':', list2.count(z))