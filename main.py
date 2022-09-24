from lib2to3.pgen2 import token
from flask import Flask, jsonify, request, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'estaeslaclavesecreta'


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if (not token):
            return jsonify({'mensaje': 'Falta el token'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'mensaje': 'token invalido'})
    return decorated


@app.route('/')
def root():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Conectado'


@app.route('/palindromo')
@token_required
def meth():
    return jsonify({'mensaje': 'Token Verificado'})


@app.route('/login', methods=['POST'])
def login():
    if (request.form['username'] and request.form['password'] == "123456"):
        session['logged_in'] = True
        token = jwt.encode({
            'user': request.form['username'],
            'expiration': str(datetime.utcnow()+timedelta(minutes=60))
        },
            app.config['SECRET_KEY'])
        return jsonify({'token': token})
    else:
        return make_response('no fue posible verificar', 403, {'WWW-Authenticate': 'Basic realm:"fallo autenticacion"'})


if __name__ == '__main__':
    app.run(debug=True)
