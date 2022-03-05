def bold(string):
    """
    This function returns a bolded string.
    """
    return "\033[1m" + string + "\033[0m"


print("=== Welcome to the BMI (Body Mass Index) calculator ===")
print("")

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))
# convert height to meters
height = height / 100

bmi = weight / (height ** 2)

bodyTypes = {
    tuple([0, 18.5]): "Underweight",
    tuple([18.5, 25]): "Normal",
    tuple([25, 30]): "Overweight",
    tuple([30, 35]): "Obese",
    tuple([35, 100]): "Extremely Obese"
}

for key, value in bodyTypes.items():
    if bmi >= key[0] and bmi < key[1]:
        print("Your BMI is about " + str(round(bmi, 2)) + " and you are " + bold(value))
        break
