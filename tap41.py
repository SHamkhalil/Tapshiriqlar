import math
import random

f_num = random.randint(100, 1000)
s_num = random.randint(100, 1000)

print(f"Birinci eded: {f_num} \n Ikinci eded: {s_num}")
print(f"EKOB: {math.lcm(f_num,s_num)}")
print(f"EBOB: {math.gcd(f_num,s_num)}")
