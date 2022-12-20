def checkZeroTwice(num):

    numStr = str(num)

    if len(numStr) < 2:
        return False
    
    for i in range(len(numStr)-1):

        if numStr[i] == '0' and numStr[i + 1] == '0':
            return True
    
    return False
import random
num = random.randint(1,10000000)
print(num)
print(checkZeroTwice(num))