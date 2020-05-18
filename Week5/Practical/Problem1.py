'''x = int(input('1st number: '))
y = int(input('2nd number: '))
z = int(input('3rd number: '))
def averfunc(x,y,z):
    a = (x+y+z)/3
    return(a)
c = int(averfunc(x,y,z))
print(c)'''



def averfunc(aversum):
    a = (x+y+z)/3
    return(a)
x = int(input('1st number: '))
y = int(input('2nd number: '))
z = int(input('3rd number: '))
print(averfunc((x,y,z)))