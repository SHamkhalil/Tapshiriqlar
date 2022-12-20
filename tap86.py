import random
randomlist = [random.randint(1,20) for i in range (11)]
print ("Random List : ",randomlist)

a = random.randint(1,5)
b = random.randint(5,10)
del randomlist[a:b] 
print ("Yeni list: ",randomlist)