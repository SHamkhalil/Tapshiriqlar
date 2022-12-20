import random

num = random.randint(100, 999)
print(num)
num_s = num // 100
print(num_s)
netice = (num - num_s*100)* 10 + num_s

print(netice)