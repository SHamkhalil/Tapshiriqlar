import random

a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(1,100)
m = random.randint(1,100)
n = random.randint(1,100)
if a * b < m * n and a * c < m * n and b * c < m * n:
    print("True")
else:
    print("False")
