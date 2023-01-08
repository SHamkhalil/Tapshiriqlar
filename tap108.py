import random

bit = random.randint(1, 10000000)

bayt = bit/(2**3)
print(f"Baytlarin sayi: {bayt}bayt")

Kb = bayt/(2*10)
print(f"Kbaytlarin sayi: {Kb}Kb")

Mb = bayt/(2*20)
print(f"Mbaytlarin sayi: {Mb}Mb")