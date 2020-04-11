list1 = ['a', 'abc', 'xyz', 's', 'aba', '1221']
list2 = [i for i in list1 if ((len(i)>2) and (i[0] == i[-1]))]
print(list1)
print(list2)
print(len(list2))