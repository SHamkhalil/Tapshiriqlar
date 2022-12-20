cumle = input("Cumle yazin: ")

wcap = []
wocap = []
num = []
letters = list(cumle)

count = 0
for i in letters:
    if letters[count].isdigit() == True:
        num.append(letters[count])
        count += 1
    else:
        wocap.append(letters[count])
        count += 1

print(f"Reqmler: {len(num)}")