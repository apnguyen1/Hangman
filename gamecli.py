from random import choice

# The Manager manages a game of hangman between a player and an AI.
class Manager:
    
    # Initializes the game of Hangman. 
    # Raises ValueError if given empty dictionary or the given word length is less than 2. 
    # Raises Exception if there are no words that are wordLength long. 
    def __init__(self, dictionary, wordLength):
        if wordLength < 2 or len(dictionary) == 0:
            raise ValueError("Game cannot be initialized with a word length less than 1 or an empty dictionary.")
                        
        self.__guesses = 7
        self.__guessedLetters = set()
        self.__words = set()
        self.__current_word = ["-"] * wordLength
        
        for word in dictionary.keys():            
            if len(word) == wordLength:
                self.__words.add(word)
        
        if len(self.__words) != 0:
            self.__target_word = choice(list(self.__words))
        else:
            raise Exception(f"There is no word of length {wordLength} in this dictionary")
        
    # Retrieves the user's amount of guesses left to find the correct word. 
    def guessesLeft(self):
        return self.__guesses
    
    # Retrieves a copy of user's guessed letters. 
    def guessedLetters(self):
        return self.__guessedLetters.copy()
    
    # Retrieves a copy of possible words in the dictionary.
    def wordsInDict(self):
        return self.__words.copy()
    
    # A helper method to test the program.
    def set_target_word(self, str):
        self.__target_word = str
    
    # Retrieves the secret/target word that the computer has choosen. 
    def get_target_word(self):
        return self.__target_word
    
    # Retrieves the current guesses that the user has made
    def get_current_word(self):
        return "".join(self.__current_word)
    
    # Determines whether the user guess is in the secret word. Adds the guessed letter to the
    # existing letters guessed, and appriopriately updates the amount of guesses left. 
    # Returns the amount of the char in the target word.
    # Raises TypeError if char is not a string.
    # Raises ValueError if char is not an alphabetical character and isn't a single letter.
    # Raises ValueError if the amount of guesses the user has is less than 1 or char has already 
    # been guessed.
    def guess(self, char):
        if type(char) != str:
            raise TypeError("Please enter the guess as a string")
        
        if len(char) != 1 or not char.isalpha():
            raise ValueError("Please enter a single, alphabetical char")
        
        if self.__guesses < 1:
            raise ValueError("Game over. No more tries")
        
        if char.lower() in self.guessedLetters():
            raise ValueError("Letter has already been guessed previously.")
        
        target = self.__target_word.lower()

        self.__guessedLetters.add(char.lower())
        count = 0
        
        if char in target:
            for index in range(0, len(target)):
                if target[index] == char:
                    self.__current_word[index] = char
                    count += 1
        else:
            self.__guesses -= 1
            
        return count
            
    def reset(self):
        self.__guesses = 7
        self.__guessedLetters.clear()
        self.__words.clear()
        self.__current_word.clear()
    
    def playAgain(self, wordLength):
        self.reset()
        
        self.__target_word = choice(list(self.__words))
        
        
        
        
    
    

    
    
    
    