cumle = input("Cumle yazin: ")

wcap = []
wocap = []
num = []
non = []
space = []
letters = list(cumle)

count = 0
for i in letters:
    if letters[count].isspace() == True:
        space.append(count)
        count += 1
    else:
        wocap.append(letters[count])
        count += 1
print(f"Movqeyleri: {space}")
