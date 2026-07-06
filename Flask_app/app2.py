from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def Course(name):
    return f"Welcome to {name} course!"

@app.route('/<int:a>,<int:b>')
def Add(a,b):
    return f"Sum of {a} and {b} is {a+b}"



app.run(debug=True)