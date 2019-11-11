x = 'AbcdEFgHi'

def stringManipulation(param):
    newList = []

    for i in list(param):
        if i.isupper():
            newList.append(i.lower())
        else:
            newList.append(i.upper())
    return ''.join(newList)

print(stringManipulation(x))
    
