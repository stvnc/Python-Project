x = range(11)

def kurangLima(param):
    if param > 5:
        return True
    else:
        return False

y = filter(kurangLima, x)
print(list(y))

z = filter(lambda a: True if a >= 5 else False, x)
print(list(z))