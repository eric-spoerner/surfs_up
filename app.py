from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'sup'

@app.route('/foo')
def foo():
    return('foo.')