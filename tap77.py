def checkPassword(password): 
    if len(password) < 8:
        return False

    upperCaseCounter = 0
    lowerCaseCounter = 0
    numCounter = 0
    specialCharCounter = 0

    for c in password:
        if c.isupper(): upperCaseCounter += 1
        elif c.islower(): lowerCaseCounter += 1
        elif c.isnumeric(): numCounter += 1
        else: specialCharCounter += 1

    if (upperCaseCounter >= 1 and lowerCaseCounter >= 3 and numCounter >= 2 and specialCharCounter >=1): 
        return True    

    else: 
        return False
parol = input("Parol: ")
print(checkPassword(parol))