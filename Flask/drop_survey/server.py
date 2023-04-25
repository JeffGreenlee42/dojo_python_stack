from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('/survey.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite_language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    return redirect('/show')

@app.route('/show')
def last_user_info():
    return render_template('show.html')

if __name__=='__main__':
    app.run(port=5001, debug=True)