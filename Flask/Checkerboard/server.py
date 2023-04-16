from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello! This is not checkerboard!  Try again?"


# level 1:
@app.route('/checkerboard')
def checkerboardy():
    return render_template("checkerboard.html")



if __name__ == "__main__":
    app.run(port=5001, debug = True)



