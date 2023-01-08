def sumfraction(n): 
    sum = 0.0
    for i in range(1, int(n)+1): 
        sum+= float((i + 3/float((3**i)))) 
          
    return sum 
n = input("Eded: ") 
print("Ededlerin cemi: " + str(sumfraction(1 + int(n))))