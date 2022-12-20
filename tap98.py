import random
list = []

for i in range(1,11):
    i = random.randint(1,100)
    list.append(i)
fulllist = list
middle = len(list)//2
leftlist = list[:middle] 
rightlist = list[middle:] 

print("Ummumi list:", fulllist)
print("Birinci yarsi: ", leftlist) 
print("Ikinci yarsi: ", rightlist)
for x in leftlist:
    rightlist.append(x)
print(rightlist)
