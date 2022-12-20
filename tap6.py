import random

num = random.randint(1000, 9999)

x = [int(x) for x in str(num)]

print(x)

if num % x[0] == 0 and num % x[1] == 0 and num % x[2] == 0 and num % x[3] == 0:
    print("Bolunur")
else:
    print("Bolunmur")