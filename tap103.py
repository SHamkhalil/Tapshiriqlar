import random
import math
menfi = random.randint(0,1)
if menfi == 0:
    x = random.random()*100*(1)
else:
    x = random.random()*100*(-1)
print(x)

if x <= 0:
    A = 0
    print(A)
elif 0<x<1:
    A = x**2-x
    print(A)
else:
    A = x**2-math.sin((math.pi*x)**2)
    print(A)