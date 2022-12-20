num = []
tthree = []
for x in range(1,101):
    num.append(x)
print(num)

n = 0
for n in range(len(num)):
    if num[n] % 3 == 0:
        tthree.append(num[n])
        n += 1

sum_t = sum(tthree)
Cem = (f"Cem: {sum(tthree)}")
print(Cem)