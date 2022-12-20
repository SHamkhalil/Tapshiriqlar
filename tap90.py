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
if len(musbet_n) != len(menfi_n):
    if len(musbet_n)>len(menfi_n):
        ferq = len(musbet_n) - len(menfi_n)
        for i in range(ferq):
            i = random.randint(-10, -1)
            ferq_l.append(i)
        menfi_n.extend(ferq_l)
    else:
        ferq = len(menfi_n) - len(musbet_n)        
        for i in range(ferq):
            i = random.randint(1, 10)
            ferq_l.append(i)
        musbet_n.extend(ferq_l)
print(f"Musbet ededler: {musbet_n}\nMenfi ededler: {menfi_n}")
