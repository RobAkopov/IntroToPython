<<<<<<< HEAD
text = input('Write: ')
if (('USA' not in text)  or ('usa' not in text)):
    print('You are rejected by USA government')
else:
    a = text.count('USA')
    b = text.count('usa')
    c = a + b
    e = text.replace('USA', 'Armenia')
    f = e.replace('usa', 'Armenia')
    print('The given string:', text)
    print('The USA/usa count is:', c)
=======
text = input('Write: ')
if (('USA' not in text)  or ('usa' not in text)):
    print('You are rejected by USA government')
else:
    a = text.count('USA')
    b = text.count('usa')
    c = a + b
    e = text.replace('USA', 'Armenia')
    f = e.replace('usa', 'Armenia')
    print('The given string:', text)
    print('The USA/usa count is:', c)
>>>>>>> 90b5633f9bd6f57998b6a7f286d2af33b42f15fc
    print('The new string:', f)