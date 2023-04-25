from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/survey.html')


if __name__=='__main__':
    app.run(port=5001, debug=True)