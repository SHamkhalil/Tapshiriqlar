repeatedlist = []
n = input("Eded: ")
mylist = [int(i) for i in str(n)]
solo = []

for i in mylist:  
    if i not in repeatedlist:  
        count = mylist.count(i)       
        if count > 1:     
            repeatedlist.append(i)
        else:
            solo.append(i)
    
print("bir defe ishtirak eded ededler : ",solo)