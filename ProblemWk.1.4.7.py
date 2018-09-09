def isPalindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    return string[0] == string[-1] and isPalindrome(string[1:-1])

print isPalindrome('aba')
print isPalindrome('able was I ere I saw elba')
print isPalindrome('a man a plan a canal panama')
    
