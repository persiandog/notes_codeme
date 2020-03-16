"""Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’)."""

txt = input("Enter greetings for me: ")

#string slicing:
print(txt[::2])

#for
new_txt = ""
count = 0

for c in txt:
    if count % 2 == 0:
        new_txt += c
    count += 1

print(new_txt)