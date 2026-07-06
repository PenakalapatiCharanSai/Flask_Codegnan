from flask import Flask


app = Flask(__name__)

# @app.route('/')
# def About():
#     return "Welcome to About page"

@app.route('/user/<name>')
def User(name):
    return f"Welcome {name}!"




app.run(debug=True)