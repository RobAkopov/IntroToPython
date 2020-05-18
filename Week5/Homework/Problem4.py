def my_func(n):
    if n < 10:
        return n + 10
    else:
        return n - 10
list1 = [21, 23, 37, 2, 1, 5, 6, 7]
list2 = map(my_func, list1)
print(list(list2))