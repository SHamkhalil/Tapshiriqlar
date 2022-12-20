import random
num_l = []
for i in range(1,10):
    i = random.randint(1,100)
    num_l.append(i)
print(num_l)

num_l += [num_l.pop(0)]
print(num_l)