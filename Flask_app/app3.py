from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Home Page!"

@app.route('/admin')
def admin():
    return "Welcome Admin!"

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return f"Hello, {name}!"
app.run(debug=True)