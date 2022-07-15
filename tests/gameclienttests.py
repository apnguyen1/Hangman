from multiprocessing.sharedctypes import Value
import unittest
import sys
sys.path.append("../Hangman")

from gamecli import Manager

class game_client_tests(unittest.TestCase):
    def setUp(self):
        file = "words.txt"
        
        self.__dict = list()
        
        with open(file, "r") as file:
            words = file.readlines()
            # seize serve sharp andrew beezy jazzy aahed Abamp poops wendy john phone mouse mice lamp superfaiclious
            for word in words:
                self.__dict.append(word.strip())
    
    def tearDown(self):
        self.dict = []
        
    # tests invalid inputs given to the game client program.
    def test_invalid_init(self):
        self.assertRaises(ValueError, Manager, (), 0)      
        self.assertRaises(ValueError, Manager, (), 1)
        self.assertRaises(ValueError, Manager, (), 3)
        self.assertRaises(ValueError, Manager, ["This", "is", "a", "test", "list"], 0)
        self.assertRaises(ValueError, Manager, ("This", "is", "a", "test", "tuple"), 0)
        self.assertRaises(ValueError, Manager, {"This", "is", "a", "test", "set"}, 0)

    # tests if there are correct amount of words in the dictionary given a word length.
    def test_correct_word_lengths(self):
        obj5 = Manager(self.__dict, 5)
        obj4 = Manager(self.__dict, 4)
        
        self.assertEqual(len(obj5.wordsInDict()), 11, "There should be 13 words with the length of 5 in the file")
        self.assertEqual(len(obj4.wordsInDict()), 3, "There should be 3 words with the length of 3 in the file")
        
    # tests if an exception is raised if no word of wordLength exists
    def test_no_word_length_exists_in_dict(self):
        self.assertRaises(Exception, Manager, self.__dict, 3)
    
    # helper to share resources for methods below
    def setUpWord(self, word):
        obj5 = Manager(self.__dict, 5)
        obj5.set_target_word(word)
        
        return obj5
    
    # determines if list to string is converted correctly.
    def test_current_word_to_string(self):
        obj5 = self.setUpWord("seize")
        
        str = obj5.get_current_word()
        
        self.assertEqual(str, "-----", "current word should be empty")
        
        obj5.guess("e")
        str = obj5.get_current_word()
        
        self.assertEqual(str, "-e--e", "current word should be -e---e")
    
    # removes immutability from function that returns mutable data.
    def test_immut_functions(self):
        obj5 = self.setUpWord("seize")
        
        letters = obj5.guessedLetters()
        dict = obj5.wordsInDict()
        
        letters.add("a")
        dict.add("thisisAwesome")
        
        self.assertFalse("a" in obj5.guessedLetters())
        self.assertFalse("thisisAwesome" in obj5.wordsInDict())
        
    
    def test_invalid_guess(self):
        obj5 = self.setUpWord("seize")
        
        self.assertRaises(TypeError, obj5.guess, ["poop"])
        self.assertRaises(ValueError, obj5.guess, "ab")
        self.assertRaises(ValueError, obj5.guess, "1")
        
        obj5.guess("a")
        self.assertRaises(ValueError, obj5.guess, "a")
        self.assertRaises(ValueError, obj5.guess, "A")

    def test_correct_guesses_left(self):
        obj5 = self.setUpWord("seize")
        obj5.guess("a")
        self.assertEqual(obj5.guessesLeft(), 6, "there are 6 guesses left")
        obj5.guess("e")
        self.assertEqual(obj5.guessesLeft(), 6, "there should still be 6 guesses left")
        obj5.guess("w")
        obj5.guess("q")
        obj5.guess("l")
        obj5.guess("p")
        obj5.guess("u")
        self.assertEqual(obj5.guessesLeft(), 1, "There should be 1 guess left")
        obj5.guess("y")
        self.assertEqual(obj5.guessesLeft(), 0, "there are no more guesses left")
        self.assertRaises(ValueError, obj5.guess, "b")
        
    

if __name__ == "__main__":
    unittest.main()