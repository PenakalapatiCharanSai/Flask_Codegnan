from flask import Flask

app = Flask(__name__)

#string converter
@app.route('/course/<name>')
def Course(name):
    print("datatye is:",type(name))
    return f"I will learn {name} course"

#integer converter
@app.route('/square/<int:a>')
def Square(a):
    print("datatype is:",type(a))
    return f"The square of {a} is {a*a}"

#float converter
@app.route('/half/<float:price>')
def Half(price):
    return f"The square of {price} is {price/2}"

#path converter
@app.route('/showfile/<path:filepath>')
def Showfile(filepath):
    return f"my file path is : {filepath}"

#uuid converter
@app.route('/item/<uuid:item_id>')
def Item(item_id):
    return f"my item id is : {item_id}"


app.run(debug=True)