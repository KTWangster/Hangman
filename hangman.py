"""  
----------------------------
An interactive Hangman Game 
----------------------------

The user gets 10 chances to guess a random word.

The user should receive feedback immediately after each guess.

The game also displays the partially guessed word after each round.


Author: Katherine Wang

 """


import random
import string
# -----------ADDED LIST (OR ARRAY?) OF WORDS AND RANDOMLY GENERATED SECRETWORD---------
# Array of 10 words.
wordList = ["copper", "unite", "decisive", "notice", "branch", "explain", "educate", "guess", "enter", "available"]

# Returns a random word from wordList
def chooseWord(wordList):
    return random.choice(wordList)

# ---------------------------

# Function returns boolean if letters of secretWord in lettersGuessed
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    '''
    for char in secretWord:
        if char in lettersGuessed:
            return True
        # Returns True if all letters of secretWord in lettersGuessed
        else:
            return False

def getGuessedWord(secretWord, lettersGuessed):
    # Empty output string
    remainingWord = " "
    for char in secretWord:
        # If letter is guessed, add it to ouput string...
        if char in lettersGuessed:
            remainingWord += char
        # ...else add an underscore.
        else:
            remainingWord += "_"
    # Return string of letters and underscores of what letters in secretWord have been guessed so far.
    return remainingWord

# When letter is guessed, remove it from the list of un-guessed letters.
def getAvailableLetters(lettersGuessed):
    # Define string as lowercase alphabet letters.
    remainingWord = string.ascii_lowercase
    # If letter in output string, replace it.
    for char in lettersGuessed:
        remainingWord = remainingWord.replace(char, '')
    # Return string representing what letters have not yet been guessed   
    return (remainingWord)

# Starts up interactive portion of game.
def hangman(secretWord):
    lettersGuessed = []
    # Lists available letters.
    lettersAvailable = []
    # Maximum incorrect guesses.
    guessesLeft = 10.
    # Line seperating instructions from interactive portion of game.
    seperationLine = "********************"

    # Welcome message.
    print ("Welcome to Hangman!")
    print ("The secret word contains " + str(len(secretWord)) + " letters.")
    print ("You have 10 guesses!")
    print (seperationLine)

    # Initialize list of available letters.
    for letter in string.ascii_lowercase:
        lettersAvailable.append(letter)

    # As long as user has guesses left and secret word has not been guessed...
    while guessesLeft > 0:
        # Prints empty spaces for unsolved letters.
        print (getGuessedWord(secretWord, lettersGuessed))
        # ...indicate how many guesses are left
        print (str(int(guessesLeft)) + " guesses left!")
        # ...and which letters are still available.
        print ("Available letters: " + getAvailableLetters(lettersGuessed))
        # Prompts user to guess a letter and makes it lowercase.
        userGuess = input("Please guess a letter: ")
        userGuess = userGuess.lower()

        # Check if user input has already been guessed.
        if userGuess in lettersGuessed:
            print("Oops, you have already guessed that letter!")
            print (getGuessedWord(secretWord, lettersGuessed))
            print(seperationLine)

        # Feedback if letter is incorrect.
        elif userGuess not in secretWord:
            # Add user guess to list of guessed letters.
            lettersGuessed.append(userGuess)
            # Subtract from limit of incorrect guesses.
            guessesLeft -= 1
            print("Oops, that letter isn't in the word!")
            # Print word result as of yet.
            print(getGuessedWord(secretWord, lettersGuessed))
            print(seperationLine)

       # Checks if user entered something other than a letter. 
        elif userGuess not in string.ascii_letters:
            print("Oops, that's not a letter!")
            print (getGuessedWord(secretWord, lettersGuessed))
            print(seperationLine)

        # Otherwise, if letter has not been guessed and is in secret word, return feedback.
        else:
            lettersGuessed.append(userGuess)
            print("Good guess!")
            print (getGuessedWord(secretWord, lettersGuessed))
            print(seperationLine)
            if str(getGuessedWord(secretWord, lettersGuessed)) == str(secretWord):
                print("Congratulations, you win!")
                break


    # If user runs out of guesses, game over!
    if guessesLeft == 0:
        print("Sorry, you ran out of guesses! The word was: " + secretWord)

secretWord = chooseWord(wordList).lower()
hangman(secretWord)