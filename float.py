def f(x):
    def g():
        x = 'abc'
        pprint('x=', x)
    def h():
        x = x
        print('z =', z)
    x = x + 1
    print('x =', x)
    h()
    g()
    print('x=', x)
    print (g)

x = 3
z = f(x)
print('x=', x)
print('z=',z)
z()


'''
def f(x):
    y = 1
    x = x + y
    print('x =', x)
    return x


x = 3
y = 2
z = f(x) 

print('z =', z)
print('x = ', x)
print('y = ', y)

'''


'''
 Newton-Rapson Algorithm
'''

#epsilon = 0.01
#y = 25.0
#guess = y/2.0
#while abs(guess*guess - y) >= epsilon:
    #guess = guess - (((guess**2)-y)/(2*guess))
#print("Square root of", y, "is about", guess)


'''
def isIn(str1, str2):
    if str1 in str2:
        return True
    elif str2 in str1:
        return False


print(isIn('Good', 'Goodness'))

'''
'''
def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName, firstName)
    else:
        print(firstName, lastName)
'''



