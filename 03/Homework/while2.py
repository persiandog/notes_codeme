"""Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie
(np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie."""

secret_num = 10

guess = int(input("Guess which number (0-20) I'm thinking of: "))

while guess != secret_num:
    print("Nope, try again!")
    guess = int(input("Guess which number (0-20) I'm thinking of: "))

if guess == secret_num:
    print("You're a mind reader!")