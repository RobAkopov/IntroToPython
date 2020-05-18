def my_func(name: str, greeting = 'Welcome to our company!'):
    if isinstance(name, str):
        print(name + greeting)
    else:
        print('Fatal Error')
my_func(name = 'James Hetfield ')