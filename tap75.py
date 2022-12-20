onalti ={'1':1, '2':2, '3':3,'4':4,
        '5':5, '6':6, '7':7, '8':8, '9':9,
        'A':10, 'B':11, 'C':12,
        'D':13, 'E':14, 'F':15}
dec_l = []

num = input("16liqda reqem: ")
num_l = [str(i) for i in str(num)]
count = 0
for i in num_l:
    dec_l.append(onalti[num_l[count]])
    count += 1
print(dec_l)
dec_l.reverse()
print(dec_l)
count = 0
sum = 0
for i in dec_l:
    cem = dec_l[count]*pow(16,count)
    sum += cem
    count += 1
print(sum)