correct_num = 5
guess = int(input('Input a integer: '))
for n in range(10):
    if guess == correct_num:
        print('That was a good guess!')
        break
    elif n == 8:
        print('Your Last Chance')
    else:
        guess = int(input('Input a integer: '))
print('Goodbye!')