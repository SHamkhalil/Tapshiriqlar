import random

num = random.randint(10000, 99999)
num_l = [int(i) for i in str(num)]
print(num)

cem = 0
for x in num_l:
    cem+= x*x*x

print(cem)