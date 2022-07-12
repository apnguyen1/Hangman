# The Manager manages a game of hangman between a player and an AI.
class Manager:
    def __init__(self, dictionary, length):
        if length < 1:
            raise Exception("Length or max arguments has to be greater than one")
                
        self.guesses = 5
        self.letters = set()
        self.words = set()
        
        for word in dictionary:
            
            if len(word) == length:
                self.words.add(word)
                
        print(self.words)
        print(self.guesses)

    def guessesLeft(self):
        return self.guesses
    
    def guesses(self):
        return self.letters
    

    
    
    
    