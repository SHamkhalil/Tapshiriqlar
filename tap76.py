gunler = []
sehir = []
num_l = []
myFinallist = []
count = 0

for i in range(1, 32):
    gunler.append(i)
for x in range(1,12):
    for i in gunler:
        sehir.append(gunler[count]*x)
        count += 1
    count = 0

for i in sehir:
    if sehir[count] < 100:
        num_l.append(sehir[count])
        count += 1

for i in num_l:
    if i not in myFinallist:
        myFinallist.append(i)
mystrlist = [str(x) for x in myFinallist]

count = 0
for i in mystrlist:
    if len(mystrlist[count]) == 1:
        mystrlist[count] = "0" + mystrlist[count]
    count += 1
soze = ["19" + x for x in mystrlist]

print(soze)
