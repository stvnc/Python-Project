class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
        self.luas = self.sisi ** 2
        self.keliling = self.sisi * 4

PersegiA = Persegi(4)
PersegiB = Persegi(8)
PersegiC = Persegi(10)

print(vars(PersegiA)); print(vars(PersegiB)); print(vars(PersegiC))