import os

print("=== Welcome to crazy simple Translator app ===")
print("Loading...")

# Check if Dictionary file is exists
dictFilePath = ".\\assignment-03\\translateList.txt"
if (os.path.exists(dictFilePath) == False):
    print("Dictionary file not found at path: " + dictFilePath)
    exit()

# Read and add all words to the memory (WORDS list)
f = open(dictFilePath, "r")
WORDS = []
list = f.readlines()
f.close()

def appendWord(en, fa):
    myDict = {
        "en": en,
        "fa": fa
    }
    WORDS.append(myDict)

for i in range(len(list) - 1):
    englishWord = list[i].strip()
    persianWord = list[i + 1].strip()
    appendWord(englishWord, persianWord)
    i += 1

print("Words list loaded.")


# Translate function to translate a sentece word by word
def translate(input, lang):
        # Translation
        userWords = input.lower().split(" ")

        translates = []
        for userWord in userWords:
            for word in WORDS:
                if userWord == word[lang["source"]]:
                    translates.append(word[lang["destination"]])
                    break
            else:
                translates.append(userWord)

        translated = " ".join(translates)
        return translated

menuId = 0
while menuId != 4:
    # Define a menu for user
    print("\n1: Add new word\n2: English (En to Fa)\n3: Farsi (Fa to En)\n4: Exit")
    print("Please choose: ")
    menuId = int(input())

    # Trying to add words to the dictionary file if it choosed
    if menuId == 1:
        addFa = input("Type word in Farsi: ").lower()
        addEn = input("Type word in English: ").lower()
        wf = open(dictFilePath, "a")
        wf.write("\n" + addEn)
        wf.write("\n" + addFa)
        wf.close()

        appendWord(addEn, addFa)

    # Translation
    if menuId in (2, 3):
        lang = {}
        if menuId == 2 :
            lang["source"] = "en"
            lang["destination"] = "fa"
        else: 
            lang["source"] = "fa"
            lang["destination"] = "en"

        print("\nPlease type a word/sentence: ")
        userInputs = input()

        userInputs = userInputs.split(".")
        translates = []
        for userInput in userInputs:
            translates.append(translate(userInput, lang))

        print("Translated: ")
        print(".".join(translates))

print("Khosh Galdi")
exit