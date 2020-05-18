def kwarg_func(user: str, **kwargs):
    if user == 'admin':
        for key, value in kwargs.items():
            print('Argument1 name: ', key, 'argument1 value: ', value)
    else:
        print('Access denied to the user ' + user)
kwarg_func('admin', k1 = 'v1', k2 = 'v2', k3 = 'v3')
kwarg_func('user')