import random 

randlist = [random.randint(1,100) for num in range(10)]
print("Original list:", randlist)
m = random.randint(1,10)
k = random.randint(1,10)
new_list = randlist[k:m].copy()
del randlist[k:m]

print("Yeni list: ", new_list)