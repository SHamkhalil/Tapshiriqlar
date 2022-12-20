import random

num = random.randint(10,99)
print(f"Bashlangic eded: {num}")
num_a = num % 10
num_b = num // 10

print(f"Sonraki eded: {num_a*10+num_b}")