import random
musbet_n = []
menfi_n = []
num_l = []
ferq_l = []
for i in range(1, 10):
    n= random.randint(-10, 10)
    num_l.append(n)

count = 0

for i in num_l:
    if num_l[count] >= 0:
        musbet_n.append(num_l[count])
        count += 1
    else:
        menfi_n.append(num_l[count])
        count += 1
print(musbet_n,menfi_n)
if abs(sum(menfi_n)) != sum(musbet_n):
    if sum(musbet_n)>abs(sum(menfi_n)):
        ferq = abs(sum(menfi_n)) - sum(musbet_n)
        num_l.append(ferq)
    else:
        ferq = abs(sum(menfi_n)) - sum(musbet_n)
        num_l.append(ferq)
print(sum(num_l))