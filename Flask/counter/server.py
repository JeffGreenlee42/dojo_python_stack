
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



if __name__ == "__main__":
    app.run(port=5001, debug = True)
