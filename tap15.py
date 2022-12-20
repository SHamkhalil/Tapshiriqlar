import random

num = random.randint(1 ,1000)
print(f"Eded: {num}")
num_l = [int(i) for i in str(num)]
num_lr = num_l.copy()
num_lr.reverse()

if num_l == num_lr:
    print("YES")
else:
    print("NO")
