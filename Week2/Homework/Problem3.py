text = input('Write some text: ')
first_word = input('Write first word: ')
second_word = input('Write second word: ')
if first_word not in text:
    print('Fatal Error')
else:
    print('The given text:', text)
    print('First Word:', first_word)
    print('Second Word:', second_word)
    print('Output string:', text.replace(first_word, second_word))
