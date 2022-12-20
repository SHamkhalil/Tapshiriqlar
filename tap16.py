import random

x = random.randint(1000, 9999)

num_l = [int(i) for i in str(x)]

print(num_l)

max_n = max(num_l)
print(max_n)