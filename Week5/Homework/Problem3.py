def my_fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return my_fib(n-1) + my_fib(n-2)
print(my_fib(9))