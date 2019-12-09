x = [
    (1, ['a', 'b', 'c'], 3),
    (4, 5, 6)
]
#List dalam tuple dapat diubah
x[0][1][2] = 'Andi'
x[0][1].append('d')
x = tuple(x)
print(x)

x = [1, 2, 3]
y = (1, 2, 3)

'''
    set / himpunan 
    1.  no indexing
    2.  duplicate elements not allowed
    3.  set is mutable, but the elements are immutable
'''
z = {1, 2, 3} 
z.add('a')
z.add(('c', 'd', 'e'))
print(z)
'''
    misal isi set adalah {1, 2, 3, 1, 2, 3} dan ingin diprint, 
    maka yang diprint adalah 1, 2, 3
'''
z.update('Andi')
z.update('andi')
z.update([6, 7, 8])
z.update({'z', 'budi'})

print('budi' in z)
z.remove('budi')
print(z)

a = set(list('abcde'))
b = set(list('defgh'))

#symmetric diff
print(a)
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print(a ^ b)
print(b ^ a)
'''
p = {1, 2, 4, 7, 9, 19}
q = {5, 6, 7, 9, 12, 16, 17, 19}
r = {3, 6, 8, 19}
print(p.intersection(q))
print(p.intersection(q).intersection(r))
print(p & q & r)
'''

p = []
q = []
r = []
s = []

for i in range(-9, 10, 1):
    s.append(i)

for i in range(-4, 5, 1):
    p.append(i)

for i in range(-7, 2, 1):
    q.append(i)

for i in range(-1, 8, 1):
    r.append(i)

print('set P ', sorted(set(p)))
print('set Q', sorted(set(q)))
print('set R', sorted(set(r)))
print('set S', sorted(set(s)))



