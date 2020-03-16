"""Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest
dłuższy niż 5 znaków oraz czy zawiera literę a. Jeśli zawiera, wszystkie
litery a podmień na z i wyświetl powstały napis."""

x = "Learninng Python is fun and easy"
z = "a" in x

if z == True:
    print(x.replace("a", "i"))

if len(x) > 5:
    print("The 'x' sentence has more than 5 characters")