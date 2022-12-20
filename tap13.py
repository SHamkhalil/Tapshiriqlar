import random
num = round(random.random()*100000)
print(f"Eded: {num}")

num_l = [int(i) for i in str(num)]

num_l.reverse()
print(f"reverse: {num_l}")
