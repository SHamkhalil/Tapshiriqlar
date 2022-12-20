import random
import math
# (-100000,100000) intervalinda bir eded seçir ve “num” deyişenine beraber edir.
num = random.randint((-100000), 100000)
f_num = abs(num)  # ededin modulu tapilir
res, power = 0, 1
print("Main Number: " + str(num))
while f_num:  # Tek ededleri qeyd edir.
   last_digit = f_num % 10
   if last_digit % 2 != 1:
       res += last_digit * power
       power *= 10
   f_num = f_num // 10

print("Even numbers: " + str(res)) # Cut ededleri consoleda yazir.
length = len(str(res))  # 1
print("length: " + str(length))
Numbers = [int(x) for x in str(res)]  # 2
print("Numbers: " + str(Numbers))
multi = math.prod(Numbers)  # 3
print("Multiplication of all numbers: " + str(multi))
G_M = pow(multi, 1 / length)# Hendesi ortasi.
print("Hendesi ortasi: " + str(G_M))
