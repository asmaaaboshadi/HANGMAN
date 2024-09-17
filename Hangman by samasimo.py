# Hang man by samasimo 

import random     

HANGMAN_PICS=   ['''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']


# LIST OF GAME WORDS 
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()



#FUNCTION TO SELECT WORD RANDOMLY 
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)    #cuz python is zero indexed  
    return wordList[wordIndex]



# DISPLAY FUNCTION 
def displayBoard(missedLetters, correctLetters, secretWord):
    print()
    print(HANGMAN_PICS[len(missedLetters)])

    print()
    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')

    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    # Display the secret word with spaces between the letters:
    for letter in blanks:
        print(letter, end =' ')
    print()
    
# to ensure the input is correct (single letter , not guessed before , in the alphapet )   
def getGuess(alreadyGuessed):
    
    while True:
        print('Please guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Only a single letter is allowed.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter from the alphabet.')
        else:
            return guess

# FUNCTION TO ASK THE PLAYER IF HE WANT TO PLAY ANOTHER ROUND OR NOT        
def playAgain():

    print('Would you like to play again? (y)es or (n)o')
    return input().lower().startswith('y')

print('|_H_A_N_G_M_A_N_|')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

# THE MAIN LOOP FOR THE GAME 
while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # THE PLAYER ENTER THE LETTER 
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check to see if the player has won:
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('You guessed it!')
            print('The secret word is "' + secretWord + '"! You win!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if the player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
    # GAME IS DONE AND PLAY AGAIN
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
