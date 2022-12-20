month = int(input("Ay: "))
day = int(input("Gun: "))

if (month == 12 and day >= 22) or (month == 1) or (month == 2):
    print("Qishdir.")
elif (month == 3 and day >= 21) or (month == 4) or (month == 5):
    print("Yazdir.")
elif (month == 6 and day >= 21) or (month == 7) or (month == 8):   
    print("Yay.")
else:
    print ("Payiz.")