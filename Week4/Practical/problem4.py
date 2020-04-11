d = {'name': 'Armen', 'age': 15, 'grades': [10, 8, 8, 4, 6, 7] }
if 'weight' in d:
    print({'weight' : 100})
else:
    n = input('Write a value: ')
    d["weight"] = n
    print(d)