import random

num_l = []
num = random.randint(1,10000)
n = 1

for n in range(1, 10000):
    if num % n == 0:
        num_l.append(n)
        n += 1
    else: 
        n += 1
print(sorted(num_l))