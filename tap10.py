import random 
num_l = []
a = random.randint(1, 101)
n = 1

for n in range(1, 101):
    if a % n == 0:
        num_l.append(n)
        n += 1
    else: 
        n += 1

print(num_l)