import random
import math

a = random.randint(1, 1000)
print(a)

num_l = [int(i) for i in str(a)]
print(sum(num_l))

hasil = math.prod(num_l)
print(hasil)
