a = [1, 4, 5, 7, 8, -2, 0, -1]
print(a[3], a[5])
a_sorted = a.copy()
a_sorted.sort(reverse = True)
b = ['grapes', 'Potatoes', 'tomatoes', 'Orange', 'Lemon', 'Broccoli', 'Carrot', 'Sausages']
b_sorted = b.copy()
b_sorted.sort()
c = a[:3] + b[3:6]
print(a)
print(a_sorted)
print(a_sorted[1:3])
print(a_sorted[3:6])
a_sorted.pop(2)
a_sorted.pop(3)
print(a_sorted)
print(b_sorted)
print(c)