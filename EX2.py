
from this import d


x = input('Enter Dictonary 1 like this "key:value," and so on:')
dList = x.split(',')
dict1 = {}
for k in dList:
    sList = k.split(':')
    i = sList[0]
    j = sList[1]
    dict1[i] = j

x = input('Enter Dictonary 2 like this "key:value," and so on:')
dList = x.split(',')
dict2 = {}
for k in dList:
    sList = k.split(':')
    i = sList[0]
    j = sList[1]
    dict2[i] = j

def combineThem(dict1, dict2):
    kList1 = dict1.keys()
    kList2 = dict2.keys()
    dictF = {}
    for k in kList1:
        if k in kList2:
            dictF[k] = int(dict1[k]) + int(dict2[k])
    return dictF

print(dict1)
print(dict2)  
combinedDict = combineThem(dict1, dict2)

print(combinedDict)