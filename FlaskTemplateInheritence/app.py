from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/about')
def About():
    return render_template('about.html')
@app.route('/contact')
def Contact():
    return render_template('contact.html')


app.run(debug=True)