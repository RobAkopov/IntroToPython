<<<<<<< HEAD
text = input('Write some text: ')
first_word = input('Write first word: ')
second_word = input('Write second word: ')
if first_word not in text:
    print('Fatal Error')
else:
    print('The given text:', text)
    print('First Word:', first_word)
    print('Second Word:', second_word)
=======
text = input('Write some text: ')
first_word = input('Write first word: ')
second_word = input('Write second word: ')
if first_word not in text:
    print('Fatal Error')
else:
    print('The given text:', text)
    print('First Word:', first_word)
    print('Second Word:', second_word)
>>>>>>> 90b5633f9bd6f57998b6a7f286d2af33b42f15fc
    print('Output string:', text.replace(first_word, second_word))