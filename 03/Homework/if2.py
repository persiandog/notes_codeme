"""Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”."""

a = int(input("Please provide an integer: "))
b = int(input("One more please: "))

c = a + b

if c > 100:
    print("The sum of the digits you provided is: ", c)

else:
    print("The end.")
