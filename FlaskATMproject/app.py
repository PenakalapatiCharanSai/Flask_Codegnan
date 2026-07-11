from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

accounts= {}

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def Create():
    acc_no=request.form['acc_no']
    name = request.form['name']
    balance = int(request.form['balance'])
    accounts[acc_no]={"name":name,"balance":balance}
    return redirect(url_for('Dashboard',acc_no=acc_no))

@app.route('/dashboard/<acc_no>')
def Dashboard(acc_no):
    data= accounts[acc_no]
    return render_template('dashboard.html',acc_no=acc_no,data=data)

@app.route('/deposit/<acc_no>',methods=['POST'])
def Deposit(acc_no):
    amount=int(request.form['amount'])
    if amount>0:
        accounts[acc_no]['balance']+=amount
        return redirect(url_for("Dashboard",acc_no=acc_no))
    else:
        return f"Invalid amount <a href='/dashboard/{acc_no}'>Please Try again</a>"
    
@app.route('/withdraw/<acc_no>',methods=['POST'])
def Withdraw(acc_no):
    amount=int(request.form['amount'])
    if 0<amount and amount<=accounts[acc_no]['balance']:
        accounts[acc_no]['balance']-=amount
        return redirect(url_for("Dashboard",acc_no=acc_no))
    else:
        return f"invalid or insufficient balance.. <a href='/dashboard/{acc_no}'>Please Try again</a>"

@app.route('/delete/<acc_no>')
def DeleteAccount(acc_no):
    accounts.pop(acc_no)
    return redirect(url_for('Home'))




app.run(debug=True)