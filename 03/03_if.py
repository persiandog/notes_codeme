"""Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry,
ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.
"""


x = (float(input("Oceń książkę w skali 1-10:")))
y = (float(input("Oceń książkę w skali 1-10:")))
z = (float(input("Oceń książkę w skali 1-10:")))

average = (x + y + z) / 3

if average > 7:
    print("Ta książka jest bardzo dobra")

elif average < 4:
    print ("Ta książka nie jest warta uwagi")

else:
    print("Ta książka jest przeciętna")

