def arg_func(name: str, *argv):
        if len(argv) > 0:  
            print(name, ' your average grade is:', int(sum(argv)/len(argv)))
        else:
            print('No grades availble for', name)
arg_func('John', 8,7,10)
arg_func('John')