from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_game_form():
    """Shows the game form"""

    play_a_game = request.args.get("selection")

    if play_a_game == "no":
        return render_template("goodbye.html")

    return render_template("game.html")

@app.route('/madlib')
def show_madlib():
    """Shows completed madlib with user inputs filled in"""

    person = request.args.get("person")
    color = request.args.get("color").lower()
    noun = request.args.get("noun").lower()
    adjective = request.args.get("adjective").lower()

    return render_template("madlib.html", person=person, color=color, noun=noun, adjective=adjective)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
