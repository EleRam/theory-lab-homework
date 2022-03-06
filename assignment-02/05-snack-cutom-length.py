print("=== Print a Snack with your desired length! ===")

inputLength = int(input("tell me the length you want: "))

char_0 = "🟨"
char_1 = "🟩"

for i in range(inputLength):
    if (i % 2 == 1):
        print(char_0, end="")
    else:
        print(char_1, end="")