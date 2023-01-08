numbers = []
for n in range(1,101):
    numbers.append(n**2+n)
    n += 1
print(f"Cem: {sum(numbers)}")