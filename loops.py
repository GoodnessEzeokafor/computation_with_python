'''
if __name__ == '__main__':
    x = int(input("Enter a number to get the square: "))
    ans = 0 # the square
    itersLeft = x # iteration
    while(itersLeft != 0):
        ans += x
        itersLeft -= 1
print(str(x) + "*" + str(x) + ' = ' +str(ans))

'''

if __name__ == '__main__':
    x = int(input("Enter the range of number e.g. 2,3,5: "))
    new_list = list(range(x))
    for i in new_list:
        if i%2 == 1:
            second_list = list(i)
            print(second_list)
        
