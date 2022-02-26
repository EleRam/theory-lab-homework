# kg to pound

# pound = kg * 2.20462262

welcomeMsg = "Welcome to the KG to Pound Converter"

print(welcomeMsg)

inputKg = float(input("Enter your weight in kg: "))    # input kg
inputKg = int(inputKg)

result = inputKg * 2.20462262

resultMsg = "`" + str(inputKg) + "` kg = `" + str(result) + "` pound"
print(resultMsg)