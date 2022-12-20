import random
number = random.randint(100,999)
print(number)
temp = number
cem = 0
while temp != 0:
    k = temp % 10
    cem += k*k*k
    temp = temp//10
if cem == number:
    print('Armstrong ededidir.')
else:
    print('Armstrong ededi deyil.')
