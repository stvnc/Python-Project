
a = ['Andi', 'Budi', 'Caca']
b = ['Apel','Jeruk', 'Nanas']

def combi(a, b):
    return a+ ' ' +b

x =  map(combi , a)

print(x)
print(list(x))