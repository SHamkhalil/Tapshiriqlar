import math

n = input("n ededi: ")
m = input("m ededi: ")
num_n = []
num_m = []
num_l = []
for i in range(1, int(n)+1):
    num_n.append(i)
    i += 1
nfa = math.prod(num_n)
for i in range(1, int(m)+1):
    num_m.append(i)
    i += 1
mfa = math.prod(num_m)
for i in range(1, int(n)-int(m)+1):
    num_l.append(i)
    i += 1
mnfa = math.prod(num_l)

netice = nfa/(mfa*mnfa)
print(f"{n} elementli coxlugun {m} elemtli alt coxluqlari: {netice} beraberdir.")