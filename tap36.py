import random
import math
num_l = []
Mul = []
for x in range(1, 11):
    x = random.randint(1, 100)
    num_l.append(x)

print(num_l)

print(f"Hasili: {math.prod(num_l)}")