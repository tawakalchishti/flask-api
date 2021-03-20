from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Menu'

@app.route('/Burger')
def name():
    return 'Burger'

@app.route('/<string:name>/<int:quantity>')
def Customorder(name , quantity):
    return 'your Custom order'+ name + 'Quantity is '+ str(quantity)


if __name__ ==  '__main__':
    app.run(debug=True)

