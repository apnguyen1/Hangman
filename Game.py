# import Hangman Game Client
from gamecli import *

if __name__ == "__main__":
    file = "words.txt"
    
    def dictProc(file):
        dict = list()
        
        with open(file, "r") as file:
            words = file.readlines()
            
            for word in words:
                dict.append(word.strip())

        return dict
    
    lettersLen = int(input("Hello, Welcome to a game of Hangman. How many letters do you want to guess in this's games word?: "))
    
    
    dict = dictProc(file)
    
    # game = Manager.Manager(dict, lettersLen)
    game = Manager(dict,lettersLen)    
    # game.randomize()
    
    word = game.randomize()
    
    print(word)
    
    game.guess("E", word)
    
    print()