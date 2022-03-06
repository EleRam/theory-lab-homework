import random

word_bank = ["python", "java", "kotlin", "javascript"]

word    = random.choice(word_bank)
wordArr = ["-"] * len(word)
success = False
userGuesses = []
userGuess = ""
wrongGuesses = 0

while wrongGuesses < 6 and success == False:

    print("\n" + " ".join(wordArr))
    
    print("Please guess a letter:")
    guess = input()

    if (guess in word and guess not in wordArr):
        print("Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                wordArr[i] = guess
    else:
        print("Wrong")
        wrongGuesses += 1
        print("You have", 6 - wrongGuesses, "guesses left")

    for i in range(len(word)):
        userGuess = "".join(wordArr)
    if userGuess == word:
        success = True
        print("You guessed the word!")
        break
    
    if wrongGuesses == 6:
        print("You lose!")
        print("You guessed: " + userGuess)
        print("The word was: " + word)
        break