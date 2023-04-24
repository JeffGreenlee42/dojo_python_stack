
# Note!  I Mightily struggled, but failed to figure out how to pass jinja variables to change HTML / CSS element attributes.
# I tried "onclick='' " with both internal and external JS files..   I tried ways of changing the attributes from Python by itself,
# The problem seems to be that when changing attributes, you must put the attributes inside of double quotes and from there it seems impossible
# to get jinja to pass a Python variable.   I would love to know how the originator of the "counter" assignment changed their button colors.

from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)

app.secret_key = "My secret key"

@app.route('/')
def counter_page():
    click_button_color = "yellow"
    click_button_text_color = "black"
    if 'refresh_count' in session:
        session['refresh_count'] += 1
        click_button_color = "blue"
        click_button_text_color = "white"
    else:
        session['refresh_count'] = 0
    print(session['refresh_count'])
    return render_template('index.html', click_button_color = click_button_color, click_button_text_color = click_button_text_color)



@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')
# @app.route('/<int:x>')
# def checkerboard_x(x):
#     return render_template("checkerboard_x.html", x=x)

# @app.route('/<int:x>/<int:y>')
# def checkerboard_xy(x, y):
#     return render_template("checkerboard_xy.html", x=x, y=y)

# @app.route('/<int:x>/<int:y>/<string:odd_color>/<string:even_color>')
# def checkerboard_xy_color(x, y, odd_color, even_color):
#     return render_template("checkerboard_xy_color.html", x=x, y=y, odd_color=odd_color, even_color=even_color)


if __name__ == "__main__":
    app.run(port=5001, debug = True)
