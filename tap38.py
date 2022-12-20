num = []
tfive = []
ffive = []
for x in range(1,101):
    num.append(x)
print(num)

n = 0
for n in range(len(num)):
    if num[n] % 5 == 0:
        tfive.append(num[n])
        n += 1
    else:
        ffive.append(num[n])
        n += 1
sum_t = sum(tfive)
sum_f = sum(ffive)
Ferq = (f"Ferq: {sum_t - sum_f}")
print(Ferq)