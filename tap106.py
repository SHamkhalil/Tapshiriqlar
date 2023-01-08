import random

pul = random.randint(10000,99999)

#  Iyrenc gorsenir amma bashqa usul tapa bilmedim
two_hundred = int(pul/200)
one_hundred = int((pul%200)/100)
fifty = int(((pul%200)%100)/50)
twenty = int(((pul%100)%50)/20)
ten = int(((((pul%200)%100)%50)%20)/10)
five = int((((((pul%200)%100)%50)%20)%10)/5)
one = int(((((((pul%200)%100)%50)%20)%10)%5)/1)

print(f"Ummumi pul sayi: {pul}")
print(f"Iki yuzlukler: {two_hundred}\nYuzlukler: {one_hundred}\nEllilikler: {fifty}\nOnluqlar: {ten}\nBeshlikler: {five}\nBirlikler: {one}")