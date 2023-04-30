from flask import Flask, request, render_template, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

# This Boolean records whether each transactgion is a net gain or loss.
# It will be used in Tuple "Activities" stored in Session list
GAIN = True
LOSS = False

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0;
        session['activities'] = []
        session['turns_left'] = 15
    print(f"Your gold amount is: {session['gold']}")
    return render_template('gold.html')

@app.route('/process_money/<min_amt>/<max_amt>', methods=['POST'])
def process_money(min_amt, max_amt):
    session['turns_left'] -= 1
    print(request.form)
    print(session["activities"])
    gold = random.randint(int(min_amt), int(max_amt))
    is_richer = GAIN
    session['gold'] += gold
    if gold >= 1:
        profit = "increased"
    else:
        profit = "decreased"
        is_richer = LOSS
    session['activities'].append((f"The {request.form['process_money']} {profit} your gold by {gold} Gold pieces!", is_richer) )
    return redirect('/')

# Below is the original solution, which I superseded by the last Sensei challange!

    # if request.form['process_money'] == 'cave':
    #     gold = random.randint(5, 10)
    #     session['gold'] += gold
    #     session['activities'].append((f"The Cave increased your gold by {gold} Gold pieces!", GAIN) )
    #     return redirect('/')

    # if request.form['process_money'] == 'house':
    #     gold = random.randint(2, 5)
    #     session['gold'] += gold
    #     session['activities'].append((f"The House increased your gold by {gold} Gold pieces!", GAIN) )
    #     return redirect('/')

    # if request.form['process_money'] == 'casino':
    #     gold = random.randint(-50, 50)
    #     is_richer = GAIN
    #     session['gold'] += gold
    #     if gold >= 1:
    #         profit = "increased"
    #     else:
    #         profit = "decreased"
    #         is_richer = LOSS
    #     session['activities'].append((f"The Casino {profit} your gold by {gold} Gold pieces!", is_richer) )
    #     return redirect('/')

@app.route("/clear")
def clear():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(port=5001, debug=True)