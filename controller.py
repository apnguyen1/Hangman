import json
from secrets import choice
from uuid import uuid1
from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="website/templates", static_folder="website/static")


# DATABASE

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///hangman.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Game(db.Model):
    gameid = db.Column(db.String(50), primary_key=True)
    word = db.Column(db.String(30))
    guesses = db.Column(db.Integer)
    letters = db.Column(db.String(26))
    
    def __init__(self, dict):
        words = open(dict).read().splitlines()
        
        self.gameid = str(uuid1())
        self.word = choice(words)
        self.guesses = 8
        self.letters = ''
        
    @property
    def current_word(self):
        word = [letter if letter in self.letters else "_" for letter in self.word]
        
        return "".join(word)

    def guess(self, letter):        
        self.letters += letter
        db.session.commit()
        
        return letter in self.word
    
# END OF DATABASE

# ROUTES

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/game", methods=["POST", "GET"])
def hangman():    
    
    if request.method == "POST":
        topic = request.form["topic"].lower()
        game = Game(topic + ".txt")
        
        db.session.add(game)
        db.session.flush()
        db.session.refresh(game)
        
        id = game.gameid
        
        gamejson = jsonify(gameid = id,
                    word = game.word,
                    guesses = game.guesses,)
        db.session.commit()
        
        return gamejson
    
    return render_template("hangman.html")

    
@app.route("/game/<string:gameid>", methods=["POST", "GET"])
def game(gameid):
    game = Game.query.get_or_404(gameid)
    
    if request.method == "POST":
        letter = request.form["letter"]
        data = game.guess(letter)
        
        return jsonify({"contains": data, "current": game.current_word})
            
    return render_template("hangman-game.html", game=game)


# END OF ROUTES


if __name__ == "__main__":
    db.session.commit()
    db.drop_all()
    
    db.create_all()
    
    app.run(debug=True)