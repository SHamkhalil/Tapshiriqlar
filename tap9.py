import random

num_l = []
for i in range(3):
    i = random.randint(-100,100)
    num_l.append(i)

print(num_l)

if num_l[0] == num_l[1] == num_l[2]:
    print(3)
if num_l[0] == num_l[1] != num_l[2]:
    print(2)
if num_l[0] != num_l[1] != num_l[2]:
    print(0)