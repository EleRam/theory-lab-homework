import re

# str = input("Enter a date (in this format: xxx/xx/xx) ")
str = "1369/02/07"
pattern = r'^\d{4}\/(0[1-9]|1[0-2])\/(0[1-9]|[12][1-9]|30|31)$'

match = re.match(pattern, str)

if (match):
    print(match.group())
else:
    print("No match.")