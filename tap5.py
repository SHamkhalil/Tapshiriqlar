import random

num = random.randint(10000, 99999)

num_o = [int(a) for a in str(num)]
print(num_o)
ard = num_o.sort()


if num == ard:
    print("Beli")
else:
    print("Xeyr")