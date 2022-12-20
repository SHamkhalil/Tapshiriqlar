for num in range(100,1000):
  sum = 0
  temp = num
  while temp > 0:
   digit = temp % 10
   sum += pow(digit,3)
   temp //= 10
num_l = []
if num == sum:
   num_l.append(num)
print(num_l)