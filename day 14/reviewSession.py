#Class
class X:
    def __init__(self, name, age):
        self.nama = name
        self.usia = age
    
    def pensiun(self):
        return 55 - self.usia
class Y(X):
    def __init__(self, name, age, city):
        X.__init__(self, name, age)
        self.kota = city

objX = X('Andi', 22)
print(objX.pensiun())
objY = Y('Budi', 23, 'Jakarta')
print(objY.pensiun())
print(objY.kota)

class Fibo:
    def fibo(self, urut):
        if urut < 2:
            return urut
        else:
            return self.fibo(urut-1) + self.fibo(urut-2)

Fibo = Fibo()
print(Fibo.fibo(11))


