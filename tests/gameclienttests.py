from multiprocessing.sharedctypes import Value
import unittest
import sys
sys.path.append("../Hangman")

from Hangman.gamecli import Manager

class game_client_tests(unittest.TestCase):
    def setUp(self):
        file = "Hangman\words.txt"
        
        self.__dict = list()
        
        with open(file, "r") as file:
            words = file.readlines()
            # seize serve sharp andrew beezy jazzy aahed Abamp poops wendy john phone mouse mice lamp superfaiclious
            for word in words:
                self.__dict.append(word.strip())
    
    def tearDown(self):
        self.dict = []
        
    def test_invalid_init(self):
        self.assertRaises(ValueError, Manager, (), 0)      
        self.assertRaises(ValueError, Manager, (), 1)
        self.assertRaises(ValueError, Manager, (), 3)
        self.assertRaises(ValueError, Manager, ["This", "is", "a", "test", "list"], 0)
        self.assertRaises(ValueError, Manager, ("This", "is", "a", "test", "tuple"), 0)
        self.assertRaises(ValueError, Manager, {"This", "is", "a", "test", "set"}, 0)

    def test_correct_word_lengths(self):
        obj5 = Manager(self.__dict, 5)
        obj4 = Manager(self.__dict, 4)
        
        self.assertEqual(len(obj5.wordsInDict()), 11, "There should be 13 words with the length of 5 in the file")
        self.assertEqual(len(obj4.wordsInDict()), 3, "There should be 3 words with the length of 3 in the file")
        
    def test_no_word_length_exists_in_dict(self):
        self.assertRaises(Exception, Manager, self.__dict, 3)
    
    def setUpWord(self, word):
        obj5 = Manager(self.__dict, 5)
        obj5.set_target_word(word)
        obj5.guess
        
        return obj5
    
    def test_invalid_guess(self):
        obj5 = self.setUpWord("seize")
        
        self.assertRaises(TypeError, obj5.guess, ["poop"])
        self.assertRaises(ValueError, obj5.guess, "ab")
        self.assertRaises(ValueError, obj5.guess, "1")


if __name__ == "__main__":
    unittest.main()