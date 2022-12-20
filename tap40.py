num = []
tthree = []
fthree = []
for x in range(1,101):
    num.append(x)
print(num)

n = 0
for n in range(len(num)):
    if num[n] % 3 == 0:
        tthree.append(num[n])
        n += 1
    else:
        fthree.append(num[n])
        n += 1
sum_t = sum(tthree)
sum_f = sum(fthree)
Nisbet = (f"Nisbet: {(sum_t / sum_f)*100}")
print(Nisbet)