import random
from words import data
import string

def randomWords(words):
    word=random.choice(words)
    return word
def hangman():
    word = randomWords(data).upper()
    wordLetters = set(word)
    alphabets = set(string.ascii_uppercase)
    usedLetters = set()

    print(f"Generated word: {word}")  
    while len(wordLetters)>0:
        print(len(wordLetters))
        print("Used letters: ", ' '.join(usedLetters))
        wordList = [letter if letter in usedLetters else '_' for letter in word]
        print('Current word:',' '.join(wordList))
        userLetter = input("Enter a letter: ").upper()
        if userLetter in alphabets - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
        elif userLetter in usedLetters:
            print("!You already guessed that letter, try another.")
        else:
            print("Invalid character. Please enter a valid letter.")
    print(f"Congratulations! The word was {word}")
        
hangman()