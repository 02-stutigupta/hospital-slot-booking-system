from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello'

@app.route('/test')
def test():
    return "this is a new page"
@app.route('/home')
def home():
    return 'this is home page'
app.run(debug = True)

