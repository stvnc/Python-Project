from flask import Flask, jsonify, send_from_directory, abort, render_template

server = Flask(__name__)

@server.route('/')
def home():
    return '<h1>Hello Guys!</h1><br><a href="/employee">ke karyawan</a>'

@server.route('/html')
def html():
    return render_template("htmlText.html") 

@server.route('/data')
def data():
    nama  = "Andi"
    kota = "Jakarta"

    return render_template(
        'data.html', data = {'name' : nama, 'city' : kota}
    )

karyawan = [
    {'id': 1, 'nama': 'Andi', 'Usia': 20, 'kota': 'Jakarta'},
    {'id': 2, 'nama': 'Budi', 'Usia': 21, 'kota': 'Jakarta'},
    {'id': 3, 'nama': 'Caca', 'Usia': 22, 'kota': 'Jakarta'},
    {'id': 4, 'nama': 'Deni', 'Usia': 23, 'kota': 'Jakarta'},
    {'id': 5, 'nama': 'Euis', 'Usia': 24, 'kota': 'Jakarta'}
]

@server.route('/employee')
def employee():
    return jsonify(karyawan)

@server.route('/employee/<int:id>')
def karyawan2(id):
    if id > len(karyawan) or id < 1:
        abort(404)
    else:
        return jsonify(karyawan[id-1])

@server.route('/file/<path:namaFile>')
def myFile(namaFile):
    return send_from_directory('storage', namaFile)

@server.errorhandler(404)
def notFound(error):
    return render_template('error.html')

if __name__ == '__main__':
    server.run(debug = True, host = 'localhost', port = 1234)