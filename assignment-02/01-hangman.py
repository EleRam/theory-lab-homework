import random

word_bank = ["python", "java", "kotlin", "javascript"]

word    = random.choice(word_bank)
wordArr = ["-"] * len(word)
success = False
userGuesses = []
userGuess = ""
wrongGuesses = 0

while wrongGuesses < 6 and not success:

    print("\n" + " ".join(wordArr))
    
    for i in range(len(word)):
        userGuess = userGuess.join(wordArr)

    print("Please guess a letter:")
    guess = input()

    if (guess in word and guess not in wordArr):
        print("Good guess!")
        wordArr[word.index(guess)] = guess
    else:
        print("Wrong")


    if wrongGuesses == 6:
        print("You lose!")
        print("You guessed: " + " ".join(userGuesses))
        print("The word was: " + word)
        break
    
    if userGuess == word:
        success = True
        print("You guessed the word!")
        break
    else:
        print("You have", 6 - wrongGuesses, "guesses left")
        wrongGuesses += 1
    




print("test", end="")