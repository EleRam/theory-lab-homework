
print(" === Type a number or `=` for result ===")

list = []
userInput = input("first number: ")

i = 1
while userInput != "=" and userInput.isnumeric():
    list.append(int(userInput))
    i += 1
    print(str(i) + " number: ", end="")
    userInput = input("")

prevNumber = list[0]
isAscending = True
for num in list:
    if (num < prevNumber):
        isAscending = False
        break

if (isAscending):
    res = " "
else:
    res = " not "

print("Array is" + res + "asscending order")

