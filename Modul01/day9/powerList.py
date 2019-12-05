x = [2, 4, 6, 8, 10]
z = map(lambda a:a**2, x)

print(list(z))

def powerList(param):
    newList = []
    for i in param:
        newList.append(i ** 2)
    return newList

print(powerList(x))
