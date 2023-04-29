from flask import Flask, request, render_template, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0;
        session['activities'] = []
    print(f"Your gold amount is: {session['gold']}")
    return render_template('gold.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    print(request.form)
    if request.form['process_money'] == 'farm':
        gold = random.randint(10, 20)
        session['gold'] += gold
        session['activities'].append(f"The Farm increased your gold by {gold} Gold pieces!" )
        return redirect('/')

    if request.form['process_money'] == 'cave':
        gold = random.randint(5, 10)
        session['gold'] += gold
        session['activities'].append(f"The Farm increased your gold by {gold} Gold pieces!" )
        return redirect('/')

    if request.form['process_money'] == 'house':
        gold = random.randint(2, 5)
        session['gold'] += gold
        session['activities'].append(f"The Farm increased your gold by {gold} Gold pieces!" )
        return redirect('/')

    if request.form['process_money'] == 'casino':
        gold = random.randint(-50, 50)
        session['gold'] += gold
        if gold >= 1:
            profit = "increased"
        else:
            profit = "decreased"

        session['activities'].append(f"The Farm {profit} your gold by {gold} Gold pieces!" )
        return redirect('/')

@app.route("/clear")
def clear():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(port=5001, debug=True)