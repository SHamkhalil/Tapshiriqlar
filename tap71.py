ay_dict = {1: 31, 2: 28, 
           3: 31, 4: 30,
           5: 31, 6: 30, 
           7: 31, 8: 31,
           9: 30, 10: 31,
           11: 30, 12: 31}

n = input(f"Ayin nomresi: ")
print(f"Hemin ayda: {ay_dict.get(int(n))} qeder gun var.")

