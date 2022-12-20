import random

num = random.randint(1,1000)
tek_n = []

num_l = [int(i) for i in str(num)]
print(f"Eded: {num}")
count = 0
for x in num_l:
    if num_l[count] % 2 == 1:
        tek_n.append(num_l[count])
        count += 1
    else:
        count += 1

print(f"Tek reqemlerin sayi: {len(tek_n)}")