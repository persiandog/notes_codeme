"""
Stwórz zmienną przechowującą
wyraz o długości nieparzystej większej niż 7 i zwróć
łańcuch złożony z trzech środkowych znaków danego ciągu.
"""
text = input("Podaj tekst o długości nieparzystej >7:")
center = len(text)//2
new_text = text [center -1] + text[center] + text [center + 1]

print(new_text)
