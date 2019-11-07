import re

text = "Hari ini hari libur nasional"

x = re.search("^Hari.*nasional$", text) #^Diawali dengan hari dan nasional$ diakhiri dengan nasional
y = re.findall("ari", text) #Mencari seluruh kata yang mengandung ari pada variabel
z = re.search("\s", text) #Mencari lokasi white space pada variabel
v = re.split("\s", text) #Memecah kata yang terpisahkan oleh space menjadi list
w = re.sub("\s", "9", text) #Mengganti space dengan angka 9

'''
    [] = set dari karakter
    \ = special sequence -> seperti \A \b \B \d dsb
    . = karakter apa saja
    ^ = diawali dengan
    $ = diakhir dengan
    * = terjadi 0 kali atau lebih
    + = terjadi 1 kali atau lebih
    {} = tepat berapa kali terjadi
    | = atau
    () = capture and group
'''

if(x):
    print("YES")
else:
    print("NO")

print(y)
print(f'The first white-space character is found in position: {z.start()}')
print(f'Split Function: {v}')
print(f'Sub Function: {w}')

print(re.findall("zzzz", text))