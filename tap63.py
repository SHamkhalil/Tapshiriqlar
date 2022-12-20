cumle = input("Cumle yazin: ")

wcap = []
wocap = []
letters = list(cumle)
count = 0

for i in letters:
    if letters[count].isupper() == True:
        wcap.append(letters[count])
        count += 1
    else:
        wocap.append(letters[count])
        count += 1



print(f"Boyuk herfler: {len(wcap)}")