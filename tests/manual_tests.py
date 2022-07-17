

import sys

sys.path.append("../Hangman")

print(sys.path)

from hangman_client import Manager


def setUp():
    file = "dict1.txt"
    
    dict = {}
    
    with open(file, "r") as file:
        words = file.readlines()
        # seize serve sharp andrew beezy jazzy aahed Abamp poops wendy john phone mouse mice lamp superfaiclious
        for word in words:
            dict.update({word.strip(): 1})
            
    return dict

print(setUp())

dict = setUp()

words = set()

for word in dict.keys():
    words.add(word)
    
print(words)

