def fib(n):
    """ assumes n an it >= 0"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def testFib(n):
    for i in range(n + 1):
        print('fib of',i, '=', fib(i))


'''
def factI(n):
    """
    Assumes that n is an int  > 0
    return n!	
    """
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res


def factR(n):
    """
     Assumes that n is an int > 0
     returns n!
    """
    if n == 1:
        return n
    return n*factR(n-1)



'''
if __name__ == '__main__':
    print(factR(3))


