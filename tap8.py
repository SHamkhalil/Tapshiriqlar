import random
number = random.randint(1000, 9999)

numset = set(str(number))
if len(numset) == 4:
  print("YES")
else:
  print("NO")