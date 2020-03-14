# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia. 

a = int(input("Please provide a number: "))
b = int(input("Please provide another number: "))

div = a / b
div_floor = a // b
div_mod = a % b

print("Thanks! I've divided the first number by the second. It gives: ", div)
print("If you're wondering how many times your second number could squeeze in the first one, it's: ", div_floor, "and the rest of this division is: ", div_mod)
