from multiprocessing.sharedctypes import Value
import unittest
import sys
sys.path.append("../Hangman")

from Hangman.gamecli import Manager

class game_client_tests(unittest.TestCase):
    
    
    def test_invalid_init(self):
        self.assertRaises(ValueError, Manager, (), 0)      


if __name__ == "__main__":
    unittest.main()