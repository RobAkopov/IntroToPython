import Productcheck

def buy(product, num, price):
    a = Productcheck.check(product, num)
    if a == True:
        return print('You bought',  product,  'and spent', num*price)
    else:
        return print('Sorry! We are out of this product.')

buy('candy', 10, 150)