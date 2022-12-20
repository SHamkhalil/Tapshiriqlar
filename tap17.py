import random

num = random.randint(10000, 99999)
num_l = [int(i) for i in str(num)]

max_n = max(num_l)
max_s = num_l.count(max_n)
print(f"{max_n} ededi {max_s} defe {num} ededinde yerleshir.")