def extractTags(s):
    L = []
    record = False
    for letter in s:
        if record == True:
            if letter == ']':
                record = False
                L += [elementOfL,]
                elementOfL = ''
            else:
                elementOfL += letter
        else:
            if letter == '[':
                record = True
                elementOfL = ''
    return L

print extractTags('[fizz] thing [/fizz] fuzz [zip]')
