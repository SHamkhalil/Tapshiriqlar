import random
numbers = []
for i in range(1,11):
    i = random.randint(-100, 100)
    numbers.append(i)

outputlist = []

for num in numbers:

    outputlist.append(num)

    if num < 0:

        outputlist.append(num**2)


print(outputlist)