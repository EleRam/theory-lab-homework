

def bold(string):
    """
    This function returns a bolded string.
    """
    return "\033[1m" + string + "\033[0m"


print("=== Input sides of triangle to check if it is valid ===")
print("")
sideA = float(input("Enter side A: "))
sideB = float(input("Enter side B: "))
sideC = float(input("Enter side C: "))

if sideA + sideB > sideC and sideA + sideC > sideB and sideB + sideC > sideA:
    result = "Valid"
else:
    result = "Invalid"

msg = "The given side lengths with " + str(sideA) + ", " + str(sideB) + ", " + str(sideC) + " are " + bold(result)
print("")
print(msg)