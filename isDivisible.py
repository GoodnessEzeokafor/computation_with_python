# An algorithm is a finite list o instruction that describes a computatio that when executed on a provided set of inputs will proceed through a set of well defined states and eventually produce an output
# A programming langiage is said t be Turing complete if it can be used to simulate a universal Turing Machine

'''
  Objects are the core things that Python programs manipulate.
  Every Object has a type that defines the kind of things that program can do woth
  object o that type
  
  In python a variable is just a name, nothing more
   An assignment statemet associates the name to the left of the = symbol with the object denoted by the expression to the right of the =
'''


'''
	x = int(input("Enter a number: "))
	if x %2 == 0:
	    if x%3 == 0:
		print("Divisible by 2 and 3")
	    else:
		print("Divisible by 2 and not by 3")
	elif x%3 == 0:
	    print("Divisible by 3 and not by 2")
'''

x = int(input("Enter a value for x:  "))
y = int(input("Enter a value for y: "))
z = int(input("Enter a value for z: "))

if x == y or x == z or y ==z:
    print("Change The values, values cannot be the same")
elif y < z:
    print("Y is the least")
elif x < y and x < z:
    print("X is the least")
else:
    print("Z is the least")


