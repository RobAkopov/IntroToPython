d = {'name': 'Armen', 'age': 15, 'grades': [10, 8, 8, 4, 6, 7] }
d2 = d.get('grades')
list(d2)
if sum(d2) / len(d2) > 7:
    print('Good job')
else:
    print('You need to work more')