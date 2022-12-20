# Function to print prime numbers
def primenumbers(N):
  
  for num in range (2,N + 1):
    isPrime = True

    #Check if number is divisible by any smaller number
    for j in range (2,num): 

      #If condition evaluates to true, then number is not prime       
      if (num % j == 0) : 
        isPrime = False            

    #Print the prime number    
    if isPrime : 
            print(f"{num}") 

      
# Calling the function with parameter N
n = input("Eded: ")    
primenumbers(int(n))