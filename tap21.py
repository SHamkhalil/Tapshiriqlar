umin = 1000
umax = 999999999 
count = 0

for num in range(umin, umax + 1): 
    order = len(str(num)) 
    sum = 0 

    tempnum = num 
    while tempnum > 0: 
        digit = tempnum % 10
        sum += digit ** order 
        tempnum //= 10

    if num == sum:
        print(f"Armstorong ededi {count}: {num}")
        count += 1