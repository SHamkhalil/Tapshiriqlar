import random

A = random.randint(1, 100) 
B = random.randint(1, 100) 
C = random.randint(1, 100) 
s_tri = [A,B,C]

if((A+B>C) and (B+C>A) and (A+C>B)):
    print(A,B,C)
    print('Yes')
    if max(s_tri)**2 == min(s_tri)**2 + (sum(s_tri)-(max(s_tri)+min(s_tri)))**2:
        print("1")
    else:
        print("0")
else:
    print("NO")