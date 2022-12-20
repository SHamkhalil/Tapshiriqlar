num_l = []
netice = 0

for i in range(1, 101):
    netice += i
    i += 1
    if netice >= 150:
        break
    
print(netice - i)