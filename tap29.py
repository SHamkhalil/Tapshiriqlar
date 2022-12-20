import random

num = random.randint(100, 999)
print(num)

num_l = [int(i) for i in str(num)]

num_l.reverse()
s=[str(x) for x in num_l]
print("".join(s))