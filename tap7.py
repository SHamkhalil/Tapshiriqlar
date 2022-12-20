import random
num = random.randint(1000, 9999)


print(num)

netice, quvvet = 0, 1 
while num:  
   son_eded = num % 10 
   if son_eded % 2 == 1:
       netice += son_eded * quvvet
       quvvet *= 10

   num = num // 10


print(netice)
