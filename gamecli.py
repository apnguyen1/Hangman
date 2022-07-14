# The Manager manages a game of hangman between a player and an AI.
from multiprocessing.sharedctypes import Value
from random import choice
import string
from typing import Type


class Manager:
    def __init__(self, dictionary, wordLength):
        if wordLength < 2 or len(dictionary) == 0:
            raise ValueError("Game cannot be initialized with a word length less than 1 or an empty dictionary.")
                        
        self.__guesses = 7
        self.__guessedLetters = set()
        self.__words = set()
        self.__current_word = [None] * wordLength
        
        for word in dictionary:            
            if len(word) == wordLength:
                self.__words.add(word)
        
        if len(self.__words) != 0:
            self.__target_word = choice(list(self.__words))
        else:
            raise Exception(f"There is no word of length {wordLength} in this dictionary")
        
    def guessesLeft(self):
        return self.__guesses
    
    def guessedLetters(self):
        return self.__guessedLetters
    
    def wordsInDict(self):
        return self.__words
    
    def set_target_word(self, str):
        self.__target_word = str
        
    def get_target_word(self):
        return self.__target_word
    
    def guess(self, char):
        if type(char) != str:
            raise TypeError("Please enter the guess as a string")
        
        if len(char) != 1 or not char.isalpha():
            raise ValueError("Please enter a single, alphabetical char")
        
        if self.__guesses < 1:
            raise ValueError("Game over. No more tries")
        
        if char in self.guessedLetters():
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
            self.__guesses -= self.__guesses
            
        return count
            
    def reset(self):
        self.__guesses = 7
        self.__guessedLetters.clear()
        self.__words.clear()
        self.__current_word.clear()
    
    def playAgain(self, wordLength):
        self.reset()
        
        self.__target_word = choice(list(self.__words))
        
        
        
        
    
    

    
    
    
    