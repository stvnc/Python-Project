from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'http://digidb.io/digimon-list/'
web = requests.get(url)
data = BeautifulSoup(web.content, 'html.parser')

#MENDAPATKAN DATA DARI TAG 'TD'
td = data.find_all('td')

list = []
List_OL = []
for i in td:
    if len(list) == 0:
        list.append(i.text[1:])
    elif len(list) == 1:
        list.append(i.text[2:])
    else:
        list.append(i.text)
        if len(list) == 13:
            List_OL.append(list)
            list = []

#MENCARI DATA DARI TAG 'img'
td_img = data.find_all('img')
td_img = td_img[2:-2]
for i in td_img:
    List_OL[td_img.index(i)].insert(14, i['src'])

#MENDAPATKAN NAMA KOLOM
col = []
th = data.find_all('th')
for i in th:
    col.append(i.text)
col[0] = 'No'
col.insert(14, 'Image')

listData = []
for i in List_OL:
    data = dict(zip(col, i))
    listData.append(data)

table = pd.DataFrame(listData)

print(listData)

# #MEMBUAT FLASK
# from flask import Flask, send_from_directory, abort, jsonify, render_template
# server = Flask(__name__)

# #home route
# @server.route('/')
# def home():
#     return render_template('html.html')

# #route response json
# @server.route('/Digi_Json')
# def json():
#     return jsonify(listData)

# #route response table
# @server.route('/Digi_Table')
# def tabel():
#     return render_template("table.html", data=table.to_html())

# if __name__ == "__main__":
#     server.run(debug = True,
#     host = 'localhost',
#     port = 1234
# )