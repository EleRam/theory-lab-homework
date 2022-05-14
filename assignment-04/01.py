import re

# str = input("Enter a phone number: ")
str = "+98-915-345-6789"
pattern = r'\+\d{1,3}-\d{3}-\d{3}-\d{4}'

match = re.match(pattern, str)

if (match):
    print(match.group())
else:
    print("No match.")
