from flask import Flask, render_template
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

@app.route("/game")
def hangman():
    return render_template("hangman.html")

@app.route("/game/play")
def game():
    obj = Manager(createDictionary("dict1.txt"))
    
    word = obj.get_current_word()
    
    return render_template("hangman-game.html", word=word)



if __name__ == "__main__":
    app.run(debug=True)