import random

num = random.randint((-100000), 100000)
f_num = abs(num)
res, power = 0, 1
print(f"Eded: {num}")
while f_num:
   last_digit = f_num % 10
   if last_digit % 2 != 0:
       res += last_digit * power
       power *= 10
   f_num = f_num // 10

length = len(str(res))
Numbers = [int(x) for x in str(res)]
sum = sum(Numbers)

print(f"Ededi orta: {sum / length}")
