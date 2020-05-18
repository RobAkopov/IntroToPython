'''def my_max(*argv):
    if len(argv) == 0:
        return'no numbers given'
    else:
        return max(argv)
print(my_max(1, 20, -1, -20, 5601, 5.5, 78, 988, 5600.99))
print(my_max())'''


def my_max(*argv):
    if len(argv) == 0:
        return 'no numbers given'
    else:
        x = sorted(list(argv))
        return x[-1]
print(my_max(1, 20, -1, -20, 10000000, 5.5, 787, 78, 988, 56))
print(my_max())