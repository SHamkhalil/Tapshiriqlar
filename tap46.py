nterms = 100

n1, n2 = 0, 1
count = 0
num = []
if nterms == 1:
   print(nterms)
   print(n1)
else:
   while count <= nterms:
       nth = n1 + n2
       num.append(nth)
       n1 = n2
       n2 = nth
       count += 1

print(num[-1]-num[-2])
