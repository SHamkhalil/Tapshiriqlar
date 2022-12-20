import random

num = random.randint(10000, 99999)
print(num)

num_l = [int(i) for i in str(num)]

Netice = ((num_l[0] + num_l[1]) - (num_l[-1] + num_l[-2]))
print(Netice)