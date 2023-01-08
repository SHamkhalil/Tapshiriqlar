def seriessum(N): 

    Sum = 0

    for n in range(1, N + 1): 

        Sum += (n ** 1/2) / ((n + 4) * (5 ** (n + 1)))
          
    return Sum 
    
n_1 = input("Eded: ") 
N = int(n_1)
print("Ededlerin cemi:", seriessum(N))