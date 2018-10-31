
if __name__ == '__main__':
    s ='1,23,2.4,3,3.90'
    total = 0
    new_str = s.split(',')
    for i in new_str:
        total = total + float(i)
    print(total)

'''
CALCULATING TH0E SQUARE ROOT OF A NUMBER

if __name__ == '__main__':
    x = int(input("Enter a number: "))
    ans = 0
    while ans**2 < abs(x):
        ans = ans + 1
    if ans**2 == abs(x):
        print('Square root of' + str(x) + ' is ' + str(ans))
    else:
        print(x, ' is not a perfect square')

'''


'''
CALCULATING THE CUBE ROOT OF AN NUMBER
if __name__ == '__main__':
    x = int(input("Enter an integer: "))
    ans = 0 # cube root
    while ans ** 3 < abs(x):
        ans = ans + 1
    if ans ** 3 != abs(x):
         print(x, 'is not a perfect cube')
    else:
        if x < 0:
            ans = -ans
        print('Cube root if' + str(x) + ' is ' + str(ans))
'''


'''
CALCULATING THE CUBE ROOT OF A NUMBER
x = int(input("Enter an integer: "))
ans = 0
while ans **3 < abs(x):
    ans = ans + 1 # increment ans
if ans ** 3 == abs(x):
    print('Cube root of ' + str(x) + ' is ' + str(ans))
else:
    print(x, 'is not a perfect square')
'''

