import random
import math

num_l = []

for i in range(1, 11):
    i = random.randint(1,100)
    num_l.append(i)
    
print(num_l)
print(math.prod(num_l))
