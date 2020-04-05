list1 = [1, 3, 5, 7, 9, 11, 13, 15]
list2 = [4, 6, 14, 11, 8, 16]
for n in list1:
    if (n in list1) and (n in list2):
        break
    print(n)