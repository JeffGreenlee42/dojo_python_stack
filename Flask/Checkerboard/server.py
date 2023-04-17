from flask import Flask, render_template

app = Flask(__name__)

# level 1:
@app.route('/')
def full_checkerboard():
    return render_template("checkerboard.html")

@app.route('/4')
def checkerboard_4by8():
    return render_template("checkerboard_4by8.html")

@app.route('/<int:x>')
def checkerboard_x(x):
    return render_template("checkerboard_x.html", x=x)

@app.route('/<int:x>/<int:y>')
def checkerboard_xy(x, y):
    return render_template("checkerboard_xy.html", x=x, y=y)

@app.route('/<int:x>/<int:y>/<string:odd_color>/<string:even_color>')
def checkerboard_xy_color(x, y, odd_color, even_color):
    return render_template("checkerboard_xy_color.html", x=x, y=y, odd_color=odd_color, even_color=even_color)


if __name__ == "__main__":
    app.run(port=5001, debug = True)



