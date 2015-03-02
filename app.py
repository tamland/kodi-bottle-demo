from bottle import Bottle, template

app = Bottle()

@app.route('/')
def index():
    return "Index"

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='World'):
    return template('<b>Hello {{name}}</b>!', name=name)

