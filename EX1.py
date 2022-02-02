
x = input('Enter a list of integer seprated by ",": ')
inList = x.split(',')





def noRepeats(inList):
    outList = []
    banList = []
    for k in inList:
        if k not in outList and k not in banList:
            outList.append(k)
        elif k in outList:
            outList.remove(k)
            banList.append(k)

    return outList


fList = noRepeats(inList)

print(fList)