def isSubstring(s1, s2): 
    if len(s1) > len(s2):
        return False
    for index in range(len(s2)-len(s1)+1):
        if matchFirst(s1, s2[index:]):
            return True
    return False

def matchFirst(s1, s2):
    if len(s1) > len(s2):
        return False
    return s1 == s2[:len(s1)]

print isSubstring('', '')
print isSubstring('', '12')
print isSubstring('1234', '45634512345')
