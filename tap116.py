import math 

def mySqrt(n): 
    x = n/3
    y = (x + (n/x)) / 2
      
    while abs(y-x) > 0.000000001: 
        x = y 
        y = (x + (n/x)) / 2

    return y

num1 = int(input("Eded : "))   

print ("%d ededin texmini koku %f" %(num1, mySqrt(num1)))
