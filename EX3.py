
def toDict(L):
    d = {}
    for k in L:
        kList = d.keys()
        if k != ' ':
            if k in kList:
                d[k.lower()] = d[k.lower()] + 1
            else:
                d[k.lower()] = 1

    return d


x = input('Whats the word? ')
inList = list(x)

megaResult = toDict(inList)

print(megaResult)