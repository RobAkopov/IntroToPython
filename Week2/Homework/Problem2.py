<<<<<<< HEAD
text = (input('Write 7 or more characters with odd number of characters: '))
if (len(text) % 2 == 0) or (len(text) < 7):
    print("You're failed")
else:
    x = int((len(text) - 3) / 2)
    y = x + 3
    z = text[:x] +text[x:y].upper() + text[y:]
    print('The old string:', text)
    print('Middle 3 characters:', text[x:y])
=======
text = (input('Write 7 or more characters with odd number of characters: '))
if (len(text) % 2 == 0) or (len(text) < 7):
    print("You're failed")
else:
    x = int((len(text) - 3) / 2)
    y = x + 3
    z = text[:x] +text[x:y].upper() + text[y:]
    print('The old string:', text)
    print('Middle 3 characters:', text[x:y])
>>>>>>> 90b5633f9bd6f57998b6a7f286d2af33b42f15fc
    print('The new string:', z)