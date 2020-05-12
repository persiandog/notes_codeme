import random

"""Stwórz grę ciepło zimno.
Komputer losuje liczbę z zakresu od 1 do 100.
Użytkownik podaje swój traf.
Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
Jeśli użytkownik zgadnie wygrywa gracz.
Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer."""

cpu_number = int(random.randint(1, 101))
user_number = int(input("Guess my number (1-100): "))
count = 0
print(cpu_number)

while count < 6:
    if user_number == cpu_number:
        print("You got it! You win!")
        exit()
    elif user_number == range(cpu_number - 10, cpu_number + 10):
        int(input("Hot! Try again:"))
    else:
        int(input("Cold! Try again: "))
    count = count + 1

if count == 6:
    print("You lose! My number was: ", cpu_number)


