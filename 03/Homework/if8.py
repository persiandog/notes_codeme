"""Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej."""

a = int(input("Please provide a number: "))
b = int(input("Please provide another number: "))
c = int(input("One more: "))

if a > b and a > c:
    print("The highest number is: ", a)
elif b > a and b > c:
    print("The highest number is: ", b)
elif c > a and c > b:
    print("The highest number is: ", c)

if a > b and a > c and b > c:
    print("Your numbers in descending order: ", a, " ", b, " ", c)
if a > b and a > c and c > b:
    print("Your numbers in descending order: ", a, " ", c, " ", b)
elif b > a and b > c and a > c:
    print("Your numbers in descending order: ", b, " ", a, " ", c)
elif b > a and b > c and c > a:
    print("Your numbers in descending order: ", b, " ", c, " ", a)
elif c > a and c > b and a > b:
    print("Your numbers in descending order: ", c, " ", a, " ", b)
elif c > a and c > b and b > a:
    print("Your numbers in descending order: ", c, " ", b, " ", a)
else:
    print("Magda you're wrong")

"""
OR easy way to sort descending:
numbers = [a, b, c]
numbers.sort(reverse = True)
print("Your numbers descending: ", numbers)
"""