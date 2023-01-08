N = input("Eded: ")
kvadrat = []

for y in range(1, int(N)+1):  # ededlerin kubunun hesablanmasi.
   kvadrat.append(y ** 2)
print(sum(kvadrat))