from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# @app.route('/<phrase>')
# def NoRoute(phrase):
#     return "Sorry! No response. Try again."

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/flask')
def flask():
    return "Hi Flask!"

@app.route('/say/michael')
def michael():
    return "Hi Michael!"

@app.route('/say/john')
def john():
    return "Hi John!"

@app.route('/repeat/<int:num>/<string:phrase>')
def repeat(num, phrase):
    return num * f"{phrase} \n"




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(host="localhost", port=5001, debug=True)    # Run the app in debug mode.

