netice = 1

for i in range(1, 101):
    netice *= i
    if netice >= 1500:
        break
    i += 1
    
print(netice/i)