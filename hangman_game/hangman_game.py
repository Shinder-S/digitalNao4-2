#The secret word the player is trying to guess
secret_word = "tandil"
lettersGuessed = ""

#The number of turns before the player loses
failureCount = 6

#Loop until the player has made too many failed attempts will break loop if they succed instead
while failureCount > 0:
    
    #Get the guessed letter from the player
    guess = input("Enter a letter: ")
    
    if guess in secret_word:
        print(f"Correct! There is one or more {guess} in the secret word")
    else:
        failureCount -= 1
        print(f"Incorrect. There are no {guess} in the secret word. {failureCount} turn(s) left")
        
    #Maintain a list of all letters guessed
    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0
    
    for letter in secret_word:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_",end="")
            wrongLetterCount += 1
    if wrongLetterCount == 0:
        print(f"Congratulations!! The secret word was: {secret_word}. You won!")
        break 

else:
    print(f"Sorry, you lost. Try again!!!!!")