menu = ['ice cream', 'chocolate', 'apple crisp', 'cookies']
dessert = input('What do you want for dessert? ')
while dessert not in menu:
    dessert = input ('Please choose another dessert: ')    
else :
    print('Your dessert will arrive in 10 minutes')