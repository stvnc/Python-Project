class Orang:
    nama = 'Budi'

class Manusia:
    def __init__(self, nama):
        self.nama = nama

class Pria(Manusia):
    def __init__(self, nama):
        super().__init__(nama)
        self.gender = "Laki-laki"

class Wanita(Manusia):
    def __init__(self, nama):
        super().__init__(nama)
        self.gender = "Perempuan"

objA = Manusia('Andi')
objB = Pria('Andi')
objC = Wanita('Lusi')
print(vars(objA))
print(vars(objB))
print(vars(objC))
