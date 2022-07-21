from uuid import uuid1
from flask import Flask, redirect, render_template, request, url_for, session
from hangman_client import Manager

app = Flask(__name__, template_folder="website/templates", static_folder="website/static")

def createDictionary(file_name):
    file = file_name
        
    dict = {}
        
    with open(file, "r") as file:
        words = file.readlines()
        # seize serve sharp andrew beezy jazzy aahed Abamp poops wendy john phone mouse mice lamp superfaiclious
        for word in words:
            dict.update({word.strip(): 1})
    
    return dict

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/game", methods=["POST", "GET"])
def hangman():
    return render_template("hangman.html")

@app.route("/game/createid", methods=["GET"])
def createid():
    id = uuid1()
    
    return str(id)
    

@app.route("/game/<string:topic>/<string:gameid>", methods=["POST", "GET"])
def game(topic, gameid):
    print(request.args)
    
    
    obj = Manager(createDictionary("dict1.txt"))
    word = obj.get_current_word()
    
    return render_template("hangman-game.html", word=word)



if __name__ == "__main__":
    app.run(debug=True)