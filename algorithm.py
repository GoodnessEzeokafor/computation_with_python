'''
Asymptotic Notation
    A formal way to talk about the relationship between the running time and they
	size of the input
	The underlying motivation is the almost any algorithm is sufficiently efficient when run on small inputs
Asymptotic notation describes the complexity of an algorithm as the size of its input approach infinity

Constant Complexity
	it indicates that the Asymptotic complexity is independent of the inputs

Lograthm Complexity

** many algorithms that deal with lists or other kinds of sequence are linear because
	the touch each element of the sequence a constant



ALGORITHMS
	SEARCh ALGORITHM
		is a method fpr finding an item or group of item with a spei=cific properties within a collection of items
		Indirection involves accessing something by first accessing something else that contains a reference to the thing intially sought


SORTING ALGORITHM 	
'''




# Binary Search
def search(L, el):
	"""
	Assumes L is a list, the elements of which are in 
	ascending order
	Retuns True if e is in L and False otherwise	
	"""
	def bSearch(L, el, low,high):
		if high == low:
			return L[low] == el
		mid = (low + high)//2
		if L[mid] == el:
			return True	
		elif L[mid] > el:
			if low == mid:
				return False
			else:
				return bSearch(L, el, low, mid - 1)
		else:
			return bSearch(L, el, mid+1, high)

	if len(L) == 0:
		return False
	else:
		return bSearch(L, el, 0, len(L) - 1)




if __name__ == '__main__':
	l = [1,2,3,4,5,6]
	el  = 2345657
	print(search(l, el))

'''
#  Search
def search(l, el):
	for i in range(len(l)):
		if l[i] == el:
			return True
		if l[i] > el:
			return False
	return False


if __name__ == '__main__':
	l = [3,4,5,56,6,70]
	el = 70
	print(search(l, el))
'''

'''
# A Program to  determinte if an element is in alist

def search(l,el):
	for i in range(len(l)):
		if l[i] == el:
			return True
	return False

if __name__ == '__main__':
	l = [1,2,3,4,5]
	el = 7
	print(search(l, el))

'''



































































































'''

def isSubset(l1, l2):
	for e1 in l1:
		matched = False
		for e2 in l2:
			if e1 == e2:
				matched = True
				break
		if not matched:
			return False
	return True

if __name__ == '__main__':
	l1 = [1,2,3,4]
	l2 = [1,2]
	print(isSubset(l1,l2))

'''
