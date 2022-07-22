from random import choice

# The Manager manages a game of hangman between a player and an AI.
class Manager:
    
    # Initializes the game of Hangman. 
    # Raises ValueError if given empty dictionary or the given word length is less than 2. 
    # Raises Exception if there are no words that are wordLength long. 
    def __init__(self, dictionary):
        if type(dictionary) is not dict or len(dictionary) == 0 :
            raise ValueError("Game cannot be initialized with an empty dictionary.")
                        
        self.guesses = 7
        self.letters_guessed = set()
        self.words = set()
        
        for word in dictionary.keys():
                self.words.add(word)

        self.secret_word = choice(list(self.words))
        self.current_word = ["-"] * len(self.secret_word)
        
    # Retrieves the user's amount of guesses left to find the correct word. 
    def guesses_left(self):
        return self.guesses
    
    # Retrieves a copy of user's guessed letters. 
    def guessed_letters(self):
        return self.letters_guessed.copy()
    
    # Retrieves a copy of possible words in the dictionary.
    def words_in_dict(self):
        return self.words.copy()
    
    # A helper method to test the program.
    def set_secret_word(self, str):
        self.secret_word = str
        self.current_word = ["-"] * len(self.secret_word)
    
    # Retrieves the secret/target word that the computer has choosen. 
    def get_secret_word(self):
        return self.secret_word
    
    # Retrieves the current guesses that the user has made
    def get_current_word(self):
        return "".join(self.current_word)
    
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
        
        if self.guesses < 1:
            raise ValueError("Game over. No more tries")
        
        if char.lower() in self.guessed_letters():
            raise ValueError("Letter has already been guessed previously.")
        
        target = self.secret_word.lower()

        self.guessed_letters().add(char.lower())
        count = 0
        
        if char in target:
            for index in range(0, len(target)):
                if target[index] == char:
                    self.current_word[index] = char
                    count += 1
        else:
            self.guesses -= 1
            
        return count
            
    # def reset(self):
    #     self.__guesses = 7
    #     self.__guessedLetters.clear()
    #     self.__words.clear()
    #     self.__current_word.clear()
    
    # def playAgain(self, wordLength):
    #     self.reset()
        
    #     self.__target_word = choice(list(self.__words))
    
    def createDictionary(file_name):
        file = file_name
            
        dict = {}
            
        with open(file, "r") as file:
            words = file.readlines()
            # seize serve sharp andrew beezy jazzy aahed Abamp poops wendy john phone mouse mice lamp superfaiclious
            for word in words:
                dict.update({word.strip(): 1})
        
        return dict
