name = 'John'
age = int(17)
password = '123456&'
if name == 'Batman':
    print('Welcome Mr.Batman!')
else:
    if age < 16:
        print('Dear', name, 'you are too young to register')
    if ('*' not in password) or ('&'  not in password):
        print('Please enter a different password')