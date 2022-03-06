import random

word_bank = ["python", "java", "kotlin", "javascript"]

word = random.choice(word_bank)
wordArr = ["-"] * len(word)
success = False
userGuesses = []
userGuess = ""
wrongGuesses = 0


def print_scaffold(wrongs):  # prints the scaffold
    if (wrongs == 0):
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif (wrongs == 1):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif (wrongs == 2):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	 |")
        print("|	 |")
        print("|")
        print("|________")
    elif (wrongs == 3):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|")
        print("|	 |")
        print("|")
        print("|________")
    elif (wrongs == 4):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|")
        print("|________")
    elif (wrongs == 5):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ ")
        print("|________")
    elif (wrongs == 6):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ \ ")
        print("|________")
        # print("\n")
        # print("The word was %s." % wd)
        # print("\n")
        # print("\nYOU LOSE! TRY AGAIN!")
        # print("\nWould you like to play again, type 1 for yes or 2 for no?")
        # again = str(raw_input("> "))
        # again = again.lower()
        # if again == "1":
        #     hangMan()
        return


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
        print_scaffold(wrongGuesses)
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


