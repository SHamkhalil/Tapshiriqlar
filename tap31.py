import random

num = random.randint(100, 999)
print(num)

num_y = num // 100
num_o = num // 10 - num_y*10
Netice = (num % 10) + (num_o * 100) + (num_y * 10)
print(Netice)