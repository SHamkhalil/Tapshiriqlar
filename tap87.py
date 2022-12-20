import random

mylist = []
for i in range(1,11):
    i = random.randint(1, 100)
    if i % 2 == 0:
        mylist.append(i)

M = random.randint(1, 100)
middle_index = int(len(mylist)/2)

f_h=mylist[middle_index:]
s_h=mylist[:middle_index]

sf_h = sum(f_h)
ss_h = sum(s_h)
if sf_h > ss_h:
    f_h.append(M)
else:
    s_h.append(M)

print(s_h)
print(f_h)
