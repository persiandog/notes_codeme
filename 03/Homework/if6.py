"""Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę
wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”."""

guess = int(input("Please choose a number between 1 and 100: "))

if guess == 59:
    print("Congratulations! You got my number!")
else:
    print("Missed it! Try again!")