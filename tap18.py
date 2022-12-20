arm_l = []
arm_nl = []
for i in range(100, 1000):
    number = i
    temp = number
    cem = 0
    while temp != 0:
        k = temp % 10
        cem += k*k*k
        temp = temp//10
    if cem == number:
        arm_l.append(number)
    else:
        arm_nl.append(number)

print(arm_l)
