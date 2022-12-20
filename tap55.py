import random
import math

num = random.randint(10000, 99999)
num_l = [int(i) for i in str(num)]

print(num)

nisbet = int(math.prod(num_l)/sum(num_l))

print(nisbet)