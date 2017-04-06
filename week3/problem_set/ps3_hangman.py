# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random, string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
#wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    return set(secretWord).issubset(lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord_copy = (len(secretWord) * '_ ')[:-1]
    secretWord_copy_list = secretWord_copy.split(' ')

    for lt in lettersGuessed:
        if lt in secretWord:
            start = 0
            while True:
                index = secretWord.find(lt, start)
                if index != -1:
                    secretWord_copy_list[index] = lt
                    start = index + 1
                else:
                    break
    new_secreWord_copy = ' '.join(secretWord_copy_list)
    return new_secreWord_copy



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alpha = string.ascii_lowercase
    alpha_list = list(alpha)
    for lt in lettersGuessed:
        if lt in alpha_list:
            alpha_list.remove(lt)
    avail_alpha = ''.join(alpha_list)
    return avail_alpha



def hangman(secretWord, times):
    '''
    secretWord: string, the secret word to guess.
    times: allow how many times to guess
    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guess_num = times
    lettersGuessed = []
    avail_letters = getAvailableLetters(lettersGuessed)
    while guess_num > 0:

        print(f'You have {guess_num} guesses left.')
        print(f'Available letters: {avail_letters}')
        guess = input('Please guess a letter: ').lower()
        success = isWordGuessed(secretWord, lettersGuessed)
        lettersGuessed.append(guess)
        getGuessWord = getGuessedWord(secretWord, lettersGuessed)
        if success:
            print('Congratulations, you won!')
            break
        elif guess in secretWord:
            if guess in avail_letters:
                getGuessWord = getGuessedWord(secretWord, lettersGuessed)
                print(f'Good guess: {getGuessWord}')
                print('-' * 20)
                avail_letters = getAvailableLetters(lettersGuessed)
            else:
                print(f'Oops! You\'ve already guessed that letter: {getGuessWord}')
                print('-' * 20)
        elif guess not in secretWord:
            if guess in avail_letters:
                getGuessWord = getGuessedWord(secretWord, lettersGuessed)
                print(f'Oops! That letter is not in my word: {getGuessWord}')
                print('-' * 20)
                avail_letters = getAvailableLetters(lettersGuessed)
                guess_num -= 1
            else:
                print(f'Oops! You\'ve already guessed that letter: {getGuessWord}')
                print('-' * 20)
    print(f'Sorry, you ran out of guesses. The word {secretWord}')



def start():
    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    print('Welcome to the game, Hangman!')
    print(f'I am thinking of a word that is {len(secretWord)} letters long.')
    print('-' * 20)
    hangman(secretWord, 8)


start()
