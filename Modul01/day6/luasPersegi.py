def luasPersegi(sisi):
    print(f'Luas persegi adalah {sisi*sisi} *tanpa return')

def luasPersegiReturn(sisi):
    return sisi*sisi

luasPersegi(int(input("Masukkan sisi persegi: ")))
returnValue = luasPersegiReturn(int(input("Masukan sisi persegi: ")))
print(f'Luas persegi adalah {returnValue} *dengan return')