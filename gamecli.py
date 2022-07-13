# The Manager manages a game of hangman between a player and an AI.
from multiprocessing.sharedctypes import Value
from random import choice
import string


class Manager:
    def __init__(self, dictionary, wordLength):
        if wordLength < 1 or len(dictionary) == 0:
            raise ValueError("Game cannot be initialized with a word length less than 1 or an empty dictionary.")
                        
        self.__guesses = 6
        self.__guessedLetters = set()
        self.__words = set()
        self.__current_word = [None] * wordLength
        self.__target_word = ['E','E','E','P','E']
        
        for word in dictionary:
            
            if len(word) == wordLength:
                self.__words.add(word)
        
        print(self.__words)
        
    def guessesLeft(self):
        return self.__guesses
    
    def guessedLetters(self):
        return self.__guessedLetters
    
    def wordsInDict(self):
        return self.__words
    
    def randomize(self):
        return choice(list(self.__words))
    
    def guess(self, char, target):
        if char in self.guessedLetters():
            raise Exception("Letter has already been guessed previously.")

        self.__guessedLetters.add(char)
        
        if char in target:
            
            for index in range(0, len(target)):
                if target[index] == char:
                    self.__current_word[index] = char
        else:
            self.__guesses -= self.__guesses
            
        print(self.__current_word)
        
        
        
        
        
    
    

    
    
    
    