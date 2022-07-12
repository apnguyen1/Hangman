from Hangman import Manager

if __name__ == "__main__":
    
    def dictProc(file):
        dict = list()
        
        with open(file, "r") as file:
            words = file.readlines()
            
            for word in words:
                dict.append(word.strip())

        return dict
    
    file = "Hangman\words.txt"
    
    lettersLen = int(input("Hello, Welcome to a game of Hangman. How many letters do you want to guess in this's games word?: "))
    
    
    dict = dictProc(file)
    
    game = Manager(dict, lettersLen)