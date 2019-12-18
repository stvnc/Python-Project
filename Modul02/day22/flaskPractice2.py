from flask import request, redirect, Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def beranda():
    return render_template('home.html')

x = [
    {'no': 1, 'nama': 'Andi'},
    {'no': 2, 'nama': 'Budi'},
    {'no': 3, 'nama': 'Caca'}
]

@app.route('/home')
def redir():
    return  redirect('/')

@app.route('/test', methods = ['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'Anda nge-GET'
    elif request.method == 'POST':
        body = request.json
        print(body['kota'])
        return jsonify({
            'status': 'Data sukses terkirim',
            'nama': body['name'],
            'kota': body['kota']
        })
    else:
        return 'Anda ngerequest aneh-aneh'

@app.route('/data')
def data():
    return jsonify(x)

@app.route('/data/<int:no>')
def datano(no):
    return jsonify(x[no-1])

if __name__ == '__main__':
    app.run(debug = True, port = 1992)