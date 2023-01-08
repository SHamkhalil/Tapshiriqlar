def calcsum(n): 
    sum = 0    
    for i in range(1, n + 1): 
        sum += (4/(i*(i+1)*(i+2))) - (4/((i+2)*(i+3)*(i+4)))     
          
    return sum  


print("Sum is",3 + calcsum(15))
