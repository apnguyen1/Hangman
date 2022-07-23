from email.policy import default
from uuid import uuid1
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="website/templates", static_folder="website/static")


# DATABASE

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///hangman.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Game(db.Model):
    gameid = db.Column(db.String(50), primary_key=True)
    word = db.Column(db.String(30))
    guesses = db.Column(db.Integer, default="8")
    
    def __init__(self, word):
        self.gameid = uuid1()
        self.word = word
    
    # def __repr__(self):
    #     return "<Game %r > " % self.gameid

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
    # game = Game("andrew")
    # db.session.add(game)
    # db.session.commit()
    
    # games = game.query.all()
    
    # print(game.query.all())
    
    # print(games)
    
    # for x in games:
    #     # db.session.query(x)
        
    #     print(db.session.query(x))
    
    return redirect(url_for('home'))

# @app.route("/game/<string:gameid>", methods=["POST", "GET"])
# def game(gameid):
    # game = Game.query.get_or_404(gameid)
    
    # word = game._word
    
    # return render_template("hangman-game.html")


# END OF ROUTES


if __name__ == "__main__":
    db.create_all()
    
    testGame = Game("POOP")
    
    print(testGame.query)
    
    # print(Game.query.all())
    
    # app.run(debug=True)