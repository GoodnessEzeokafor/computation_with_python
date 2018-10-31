def isPalindrome(s):
    """
     Assumes s i a str
     Returns True if s is a palindrome and False otherwise.
     Punctuations marks, blanks and capitalization are ignored
    """
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
 


def toChars(s):
    s = s.lower()
    ans = ''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            ans  = ans + c
    return ans

def isPal(s):
    print('   isPal called with', s)
    if len(s) <= 1:
        print('  About to return True from base case')
        return True
    else:
        ans = s[0] == s[-1] and isPal(s[1:-1])
        print(' Abour to return', ans, 'for', s)
        return ans
print(toChars('GOODNESS'))

print(isPal(toChars('hannah')))

