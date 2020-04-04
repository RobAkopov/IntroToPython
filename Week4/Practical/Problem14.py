list1 = ['a', 'abc', 'xyz', 's', 'aba', '1221']
list2 = []
c = 0
for i in range (len(list1)):
    if len(list1[i]) >= 2:
       list2.append(list1[i])
for k in range (len(list2)):
    if list2[k][0]==list2[k][-1]:
        print(list2[k])
        c += 1
print(c)