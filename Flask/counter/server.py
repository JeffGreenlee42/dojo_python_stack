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
    return render_template('index.html')

def count_button():
    
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def count(refresh_count):
    session[refresh_count] += 1
    print(session)
    return render_template("count.html", refresh_count = refresh_count) 

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
