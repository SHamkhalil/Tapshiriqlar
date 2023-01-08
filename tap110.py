N = input("Eded: ")
kub = []

for y in range(1, int(N)+1):  # ededlerin kubunun hesablanmasi.
   kub.append(y ** 3)
print(sum(kub))