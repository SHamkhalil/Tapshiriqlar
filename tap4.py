import random

def Palindrome(s):
    return s == s[::-1]
 
 
num = random.randint(1000,9999)
print(num)
res = Palindrome(str(num))
 
if res:
    print("Beli")
else:
    print("Xeyr")