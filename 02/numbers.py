#Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.


combustion = 6.4 / 100
distance = 120
price_l = 5.04

total = combustion * distance * price_l

print (round(total, 2))

combustion = float (input ("Enter combustion rate per 100 km: "))
distance = int (input("Enter distance: "))
price_l = float (input("Enter price per l: "))
total = combustion * distance /100 * price_l
print ("You need ", total)