import random
numbers = []
for num in range(11):
    num = random.randint(-10,10)
    numbers.append(num)
print(f"Original list: {numbers}")

sumofelements = sum(numbers)  
print(sumofelements)

positiveelements = len([x for x in numbers if x > 0])
print(positiveelements)

numbers.insert(0, sumofelements)   
numbers.insert(1, positiveelements)


print("Yeni list: ", numbers)
