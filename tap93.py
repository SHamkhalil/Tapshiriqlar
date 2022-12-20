import random

num_l = []
for i in range(1, 10):
    n= random.randint(-10, 10)
    num_l.append(n)
count = 0
print(num_l)
if num_l[count] > 0:
    for i in num_l:
        if num_l[count] < num_l[count+1]:
            count += 1
            print('YES')
            break
        else:
            print("NO")
            break
else:
    print("NO")