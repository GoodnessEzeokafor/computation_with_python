if __name__ == '__main__':
    x = int(input("Enter a value for x: "))
    pwr = 1
    root = 0
    while pwr <= 6 and  pwr > 0:
        pwr += 1	
        while root ** pwr < abs(x):
            root += 1
        if root ** pwr == abs(x):
            print("Root of", str(x), 'is', root, "Raised to the power", pwr)


 
