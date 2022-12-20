import random

#sqrt(p(p-a)(p-b)(p-c)) p = (a+b+c)/2

a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(1,100)
p = (a+b+c)/2
if a+b > c and b+c>a and c+a>b:
    sahe = (p*(p-a)*(p-b)*(p-c))**(1/2)
    print(f"Sahe: {sahe}")
else:
    print("Ucbucaq deyil.")