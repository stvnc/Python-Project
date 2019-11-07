'''
    A lambda function is a small anonymous function.
    A lambda function can take any number of arguments, but can only have one expression.
'''
x = lambda a: a * 100
print(x(int(input('Input angka yang diinginkan: '))))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))