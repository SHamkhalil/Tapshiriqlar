import math

num_l = []
n = input("Eded: ")
for i in range(1, int(n)+1):
    num_l.append(i)
    i += 1

print(f"{n} ededinin faktoriali: {math.prod(num_l)}")