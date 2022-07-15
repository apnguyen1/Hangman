left(self):
        obj5 = self.setUpWord("seize")
        obj5.guess("a")
        self.assertEqual(obj5.guessesLeft(), 6, "there are 6 guesses left")