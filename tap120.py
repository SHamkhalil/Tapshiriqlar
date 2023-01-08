num_l = []
n = input()

for i in range(1, 100):
    num_l.append(eval(n)**i)
    i += 1

netice = (1-2/3) + sum(num_l)
print(sum(num_l))
