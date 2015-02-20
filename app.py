from bottle import Bottle, template

app = Bottle()

@app.route('/')
def index():
    return "Index"

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='World'):
    return template('<b>Hello {{name}}</b>!', name=name)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

