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
    letters = db.Column(db.String(26))
    
    def __init__(self, dict):
        words = [word.upper() for word in open(dict).read().splitlines() if len(word) > 2 and word.isalpha()]
        self.gameid = str(uuid1())
        self.word = choice(words)
        print(self.word)
        self.letters = ''
        
    @property
    def current_word(self):
        word = [letter if letter in self.letters else "_" for letter in self.word]
        return word
    
    @property 
    def errors(self):
        errors = set(self.letters).difference(set(self.word))
        return len(errors)
    
    @property
    def lost(self):
        return self.errors >= 8
    
    @property
    def won(self):
        return "".join(self.current_word) == self.word    

    def guess(self, letter):  
        guess = letter.upper()
        self.letters += guess
        db.session.commit()
        
        return guess in self.word
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
        
        gamejson = jsonify(gameid = game.gameid,)
        db.session.commit()
        
        return gamejson
    
    return render_template("hangman.html")

    
@app.route("/game/<string:gameid>", methods=["POST", "GET"])
def game(gameid):
    game = Game.query.get_or_404(gameid)
    
    if request.method == "POST":
        letter = request.form["letter"]
        
        return jsonify(contains = game.guess(letter),
                       current = game.current_word,
                       errors = game.errors,
                       lost = game.lost,
                       won = game.won)
            
    return render_template("hangman-game.html", game=game)


# END OF ROUTES


if __name__ == "__main__":
    db.session.commit()
    db.drop_all()
    
    db.create_all()
    
    app.run(debug=True)