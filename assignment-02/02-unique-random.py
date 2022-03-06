import random

count = int(input("Count of random numbers? \n"))

list = []

def getUniqueRandom(list):
    rnd = random.randint(0, 100)
    if (rnd in list):
        return getUniqueRandom(list)
    return rnd

for i in range(count):
    rnd = getUniqueRandom(list)
    list.append(rnd)

print("Unique Random Array:")
print(list)