mylist = [1, 2, 0, 4, 5]

newlist = []
i=0 
for num in mylist:
    if i<2:
        newlist.append(num)
    else:
        if num ==0 :
            total = mylist[i-2] + mylist[i-1]

            newlist.append(total)
        else:
            newlist.append(num)
    i+=1 
 
print (newlist)
