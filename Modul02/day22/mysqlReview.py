from flask import Flask, jsonify, request, render_template, redirect
import mysql.connector as mc

app = Flask(__name__)

myDb = mc.connect(
    host = 'localhost',
    user='root', 
    passwd = 'vincent28',
    database = 'testing'
)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/form', methods = ['POST'])
def form():
    if request.method == 'POST':
        body = request.form
        cursor = myDb.cursor()
        data = (body['nama'], body['usia'])
        insertQuery = f'insert into datadiri (nama, usia) values {data}'
        cursor.execute(insertQuery)
        myDb.commit()
        return redirect('/data')    

@app.route('/data', methods = ['GET', 'POST'])
def dataMethod():
    if request.method == 'GET':
        cursor = myDb.cursor()
        selectQuery = 'SELECT * from datadiri'
        cursor.execute(selectQuery)
        value = cursor.fetchall()
        value = list(map(lambda  i: {
            'id': i[0],
            'nama': i[1],
            'usia': i[2]
        }, value))
        return jsonify(value)
    elif request.method == 'POST':
        body = request.json
        cursor = myDb.cursor()
        data = (body['nama'], body['usia'])
        insertQuery = f'insert into datadiri (nama, usia) values {data}'
        cursor.execute(insertQuery)
        myDb.commit()
        return 'POST'


@app.route('/data/<int:no>', methods = ['GET', 'PUT', 'DELETE'])
def getDataWID(no):
    cursor = myDb.cursor()
    selectQuery = f'SELECT * from datadiri where id = {no}'
    cursor.execute(selectQuery)
    value = cursor.fetchall()
    value = list(map(lambda  i: {
        'id': i[0],
        'nama': i[1],
        'usia': i[2]
    }, value))
    return jsonify(value)

if __name__ == '__main__':
    app.run(debug = True, port = 2000)

