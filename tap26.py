import random

num = random.randint(100, 999)
print(num)
num_b = str(num // 10)
num_a = str(num % 10)
print(f"Eded: {num_b} {num_a}")