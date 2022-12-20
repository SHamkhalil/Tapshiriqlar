import random
musbet_n = []
menfi_n = []
num_l = []
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
n_musbet = [i ** 2 for i in musbet_n]
n_menfi = [i ** 3 for i in menfi_n]
print(f"Musbet ededlerin kvadrati: {n_musbet}\nMenfi ededlerin kubu: {n_menfi}")