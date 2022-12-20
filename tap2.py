import random

a = random.uniform(-100, 100)
b = random.uniform(-100, 100)

#Before change
print(f"a is: {a}")
print(f"b is: {b}")

x = min(a,b)
y = max(a,b)
# After change
x = (a+b)/2
y = (a+b)*2
print(f"a is: {x}")
print(f"b is: {y}")
