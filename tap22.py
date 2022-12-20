import random

# (999,999999) intervalında bir ədəd seçir və “num” dəyişəninə bərabər edir.
num = random.randint(999, 999999)
netice, quvvet = 0, 1 
print(num)  # Ədədi print edir.
while num:  # Tək ədədləri qeyd edir.
   son_eded = num % 10 
   if son_eded % 2 == 1:
       netice += son_eded * quvvet
       quvvet *= 10

   num = num // 10

print(netice)  # Nəticəni print edir.