from flask import Flask
from login import login

app=Flask(__name__)


@app.route('/',methods=['GET'])

def hello():
    return 'Hola mundo'


if __name__=="__main__":
    app.run(host = '0.0.0.0',debug =True,port=5001)
