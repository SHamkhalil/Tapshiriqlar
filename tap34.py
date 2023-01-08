x1 = int(input("X1:"))
x2 = int(input("X2:"))
y1 = int(input("Y1:"))
y2 = int(input("Y2:"))
Hell1 = int(input("Hell1:"))
Hell2 = int(input("Hell2:"))

detA = x1*y2-x2*y1
detx = Hell1*y2-Hell2*y1
dety = Hell1*x2-Hell2*x1

print(f"x = {detx/detA}\ny = {dety/detA}")