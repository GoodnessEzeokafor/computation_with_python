'''
  A Program that checks if the inputs are Odd and check the largest among the threer
  input
'''
if __name__ == '__main__':
    print("""
        Enter Three Values For X Y Z
    	 """
    )
    x = int(input("Enter a value for X: "))
    y = int(input("Enter a value for Y: "))
    z = int(input("Enter a value for Z: "))
    
    if x%2 == 1 and y%2 == 1 and z%2 == 1:
        print("All numbers are odd")
        if x > y and x > z:
          print("X is greater")
        elif y > z:
            print("Y is greater")
        else:
            print("Z is greater")
    else:
        print("All the numbers are not odd")

