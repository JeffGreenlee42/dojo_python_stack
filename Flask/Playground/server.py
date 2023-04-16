from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Who ARE you? "

@app.route('/success')
def success():
    return "Success!";

# level 1:
@app.route('/play')
def play():
    return render_template("playground_1.html")

# level 2:
@app.route('/blocks/<int:num>')
def number_of_blocks(num):
    return render_template("playground_2.html", num=num)

# Level 3
@app.route('/blocks/<int:num>/<string:color>')
def pick_color(num, color):
    return render_template("playground_3.html", num=num, color=color)

# Ninja challenge:
@app.route('/playground')
@app.route('/playground/<int:num>')
@app.route('/playground/<int:num>/<string:color>')
def playground(num=0, color=''):
    return render_template("playground_4.html", num=num, color=color)


if __name__ == "__main__":
    app.run(port=5001, debug = True)



