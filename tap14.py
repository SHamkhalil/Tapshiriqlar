import random

num = random.randint(1,100000)
print(num)
num_l = [int(i) for i in str(num)]
fiven = []
n = 0
for i in num_l:
    if num_l[n] % 5 != 0:
        fiven.append(num_l[n])
        n += 1
    else:
        n += 1

print(fiven)