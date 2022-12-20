import random
num_l = []
for i in range(1, 101):
    n = random.randint(1, 10000)
    num_l.append(n)
min = min(num_l)
index  = num_l.index(min)

print(f"Ededler: {num_l}")
print(f"Eded: {min} \nYerleshmesi: {index}")