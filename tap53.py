import random

num = random.randint(10000, 99999)
num_l = [int(i) for i in str(num)]
print(num_l)
max_e = num_l.count(min(num_l))

print(max_e)