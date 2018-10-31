def f(x):
	ans = 0# initial value
	for i in range(1000):
		ans += 1	
	print("NUmber of additions so far", ans)
	

	# Loops that takes X time	
	for i in range(x):
		ans += 1
	print("NUmber of additions so far", ans)
	
	for i in range(x):
		for j in range(x):
			ans += 1
			ans += 1
	print("Number of additions so far", ans)
	return ans



if __name__ == '__main__':
	x = int(input('Enter a number: '))	
	print(f(x))


'''
def squareRootExhaustive(x, epsilon):
	step = epsilomn ** 2
	ans = 0.0
	while abs(ans**2 - x) >= epsilon and ans <= max(x, 1):
		ans += step
	return ans

def squareRootBi(x, epsilon):
	low = 0.0
	high = max(1.0, x)
	while abs(ans**2 - x) >= epsilon:
		if ans **2 < x:
			low = ans
		else:
			high = ans
		ans = (high + low)/2.0
	return ans
'''

'''
def fact(n):
	answer = 1
	while n > 1:
		answer *= n
		n -= 1
	return answer


if __name__ == '__main__':
	n = int(input('Enter a number: '))
	print(fact(n))

'''

'''
def linearSearch(L, X):
	for e in L:
		if e == X:
			return True
		else:
			return False



if __name__ == '__main__':
	print(linearSearch('goodness', 'o'))



'''	

'''
def f(i):
	answer = 1
	while i >= 1:
		answer *= i
		i -= 1
	return answer

if __name__ == '__main__':
	num = int(input("Enter a number: "))
	print(f(num))


'''
