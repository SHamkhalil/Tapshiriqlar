import random
import math

num = random.randint(10000, 99999)
num_l = [int(i) for i in str(num)]
print(num)
print(math.prod(num_l))