listBilangan = []

def bilanganCacah(param):
    if param >= 0:
        listBilangan.append("Bilangan Cacah")

def bilanganPrima(param):
    if param > 1:
        if param == 2:
            status = True
        else:
            for i in range(2, param):
                if param % i == 0:
                    status = False
                    break
                else:
                    status =  True
    else: 
        status =  False
    if status == True:
        listBilangan.append("Bilangan Prima")

def bilanganGanjil(param):
    if param%2==1:
        listBilangan.append("Bilangan Ganjil")

def bilanganGenap(param):
    if param%2==0:
        listBilangan.append("Bilangan Genap")

def bilanganAsli(param):
    if param!=0 and param > 0:
        listBilangan.append("Bilangan Asli")

def bilanganBulat(param):
    if type(param)!= float:
        listBilangan.append("Bilangan Bulat")

def bilanganNegatif(param):
    if param < 0:
        listBilangan.append("Bilangan Negatif")

def bilanganKomposit(param):
    for i in range(1, param):
        if param%i==0:
            factor = i
    if factor > 1:
        listBilangan.append("Bilangan Komposit")

def bilanganNol(param):
    if param == 0:
        listBilangan.append("Bilangan Nol")

userInput = int(input('Masukkan angka yang ingin dicek: '))

bilanganNegatif(userInput)
bilanganGenap(userInput)
bilanganGanjil(userInput)
bilanganAsli(userInput)
bilanganBulat(userInput)
bilanganCacah(userInput)
bilanganNol(userInput)
bilanganPrima(userInput)
bilanganKomposit(userInput)

print(listBilangan)
# filteredNumber = filter(bilanganPrima, filter(bilanganCacah, filter(bilanganAsli, filter(bilanganBulat, filter(bilanganGanjil, filter(bilanganGenap, filter(bilanganNol, filter(bilanganNegatif, userInput))))))))