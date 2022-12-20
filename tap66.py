cumle = input("Cumle yazin: ")

wcap = []
wocap = []
num = []
non = []
letters = list(cumle)

count = 0
for i in letters:
    if letters[count].isalnum() != True:
        non.append(letters[count])
        count += 1
    else:
        wocap.append(letters[count])
        count += 1
print(non)
print(f"Simvolar ve boshluqlar: {len(non)}")