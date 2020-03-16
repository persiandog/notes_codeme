"""Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
(N podane przez użytkownika, ale nie większe niż 8)."""

N = int(input("Enter a natural number, equal to or lower than 8: "))
if N > 8:
    print("Error: Please provide a number equal to or lower than 8!")
    exit()

factorial = 1
if N == 0:
    print("Factorial of ", N, "is: 0*1 = 1")
if N >= 1:
    for i in range(1, N + 1):
        factorial = factorial * i
print("Factorial of", N, "is:", factorial)