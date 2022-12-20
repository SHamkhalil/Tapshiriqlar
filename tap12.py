import random
powtwo = []
num = random.randint(1,1025)
print(num)
for n in range(1, 11):
    powtwo.append(2**n)
    n += 1
print(powtwo)

if num in powtwo:
    print("YES")
else:
    print("NO")