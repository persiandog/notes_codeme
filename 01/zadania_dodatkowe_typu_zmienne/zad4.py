# Zadanie 4
# Napisz skrypt, który zapyta użytkownika o trzy liczby całkowite,
# a następnie pomnóż dwa pierwsze. przed podzieleniem wyniku przez trzecią liczbę. 
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

a = int(input("Please provide an integer: "))
b = int(input("Please provide another integer: "))
c = int(input("Please provide one more: "))

output = (a * b) / c

print("Your magic number is: ", output)
