from email.policy import default
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="website/templates", static_folder="website/static")


# DATABASE

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///hangman.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Game(db.Model):
    _gameid = db.Column("id", db.Integer, primary_key=True)
    _word = db.Column(db.String(30))
    _guesses = db.Column(db.Integer, default="10")
    
    def __init__(self, word):
        self._word = word

# END OF DATABASE

# ROUTES

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/game", methods=["POST", "GET"])
def hangman():    
    return render_template("hangman.html")


@app.route("/play", methods=["POST"])
def play():
    game = Game("andrew")
    db.session.add(game)
    db.session.commit()
    
    return redirect(url_for('game', gameid=game._gameid))

@app.route("/game/<string:gameid>", methods=["POST", "GET"])
def game(gameid):
    game = Game.query.get_or_404(gameid)
    
    word = game._word
    
    return render_template("hangman-game.html", word=word)


# END OF ROUTES


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)