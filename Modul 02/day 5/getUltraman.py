import requests as rq
from bs4 import BeautifulSoup as bs

url = rq.get('http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/')
data = bs(url.content, 'html.parser')

def isNumeric(param):
    try: 
        int(param)
        return True
    except ValueError:
        return False

for i in data.find_all("strong"):
    newString = list(i.text)
    if isNumeric(str(newString[0])):
        print(i.text)  

out = []
for i in data.find_all("strong"):
    out.append(i.text)

ultra = out[2:36]
monster = out[37:110]
for i in ultra:
    print(i)
for i in monster:
    print(i)

