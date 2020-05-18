l1 = [1,2,3,4,5,6,7,8,10,11,45,68,61,18]
def even_func(l1):
    e = [i for i in l1 if i % 2 == 0]
    return e
print(len(even_func(l1)))