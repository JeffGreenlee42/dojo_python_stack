from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    return "Success!";

@app.route('/hello/<string:bananna>/<int:num>')
def hello(bananna, num):
    return render_template("hello.html", bananna=bananna, num=num)



if __name__ == "__main__":
    app.run(port=5001, debug = True)
