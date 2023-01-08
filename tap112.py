import random

numbers = []  # ededlerin listi.
kvadrat = []  # ededlerin kvadrata getirilmesi.
kub = []  # ededlerin kuba getirilmesi.
n = 1

while n < random.randint(10, 20):
   numbers.append(n)
   n += 1
print(numbers)

for x in numbers:  # ededlerin kvadratinin hesablanmasi.
   kvadrat.append(x ** 2)
   kvadrat_sum = sum(kvadrat)
print(kvadrat)
print("Cemi: " + str(kvadrat_sum))
for y in numbers:  # ededlerin kubunun hesablanmasi.
   kub.append(y ** 3)
   kub_sum = sum(kub)
print(kub)
print("Cemi: " + str(kub_sum))
print("kvadratin kuba olan faiz nisbeti: " + str((kvadrat_sum/kub_sum)*100))  # Faizin hesablanmasi
