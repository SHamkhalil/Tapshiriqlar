year = int(input("Il: "))

if (year % 400 == 0):
    print("Bu uzun ildir.")
    
elif (year % 100 != 0) and (year % 4 == 0): 
    print("Bu uzun ildir.") 
    
else:
    print("Bu uzun il deyil.")  
    

century = (year // 100) + 1

print("Bu il: ",century,"esre aidir.")