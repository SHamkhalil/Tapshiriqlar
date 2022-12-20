import random 

randlist = [random.randint(1,100) for num in range(10)]
print("Original list:", randlist)
m = random.randint(1,10)
k = random.randint(1,10)
del randlist[k:m] 

print("Yeni list: ", randlist)