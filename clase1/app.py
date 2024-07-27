from flask import Flask 

app = Flask(__name__)

@app.route('/')

def saludar():
    return 'Hola Dario xd'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
