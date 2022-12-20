import random
num_l = []
for i in range(1, 101):
    n = random.randint(1, 10000)
    num_l.append(n)
max = max(num_l)
index  = num_l.index(max)

print(f"Ededler: {num_l}")
print(f"Eded: {max} \nYerleshmesi: {index}")