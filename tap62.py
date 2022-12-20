import math
num_l = []
for i in range(10000, 100000):
    num_l.append(i)

cavab = []
count = 0
for l in num_l:
    temp_num = [int(x) for x in str(num_l[count])]
    if sum(temp_num) == math.prod(temp_num):
        cavab.append(int(''.join(map(str,temp_num))))
    count += 1

print(cavab)