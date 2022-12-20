import random

num = random.randint(10000, 99999)
num_l = [int(i) for i in str(num)]
print(num)

cem_2 = 0
cem_3 = 0
for x in num_l:
    cem_2+= x*x
for x in num_l:
    cem_3+= x*x*x
qaliq = cem_3 % cem_2
print(cem_3)
print(cem_2)
print(qaliq)