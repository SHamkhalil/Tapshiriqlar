import random

while True:

        A = random.randint(1, 100) 
        B = random.randint(1, 100) 
        C = random.randint(1, 100) 

        if((A+B>C) and (B+C>A) and (A+C>B)):
                print(A,B,C)
                print('Yes')

        break

