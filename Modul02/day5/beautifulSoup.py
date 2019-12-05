from bs4 import BeautifulSoup
import requests as rq
# data = BeautifulSoup(
# #     open('htmlPractice.html', 'r'), 'html.parser'
# )

web = rq.get('http://127.0.0.1:5500/Modul%2002/day%205/htmlPractice.html')
data = BeautifulSoup(web.content, 'html.parser')

print(data.prettify()) #Print keseluruhan elemen dari dokumen 
print(data.title) #Print keseluruhan elemen dari title
print(data.title.text) #Ambil Text dari titlenya
print(data.title.string) #Seluruh konten dijadikan string
print(data.title.name) #Name untuk mengambil tagnya -> Title
print(data.find_all('li')[0]) #Mengambil seluruh data dari li dengan index 0
print(data.ul) #Print keseluruhan isi ul

ul = data.ul
for i in ul.find_all('li'):
    print(i.text)

for i in data.find_all('li', class_="student"):
    print(i.text)

