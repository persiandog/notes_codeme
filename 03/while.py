"""Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit"""

fahrenheit = 0
while fahrenheit <= 200:
    celsjusz = C = 5 / 9 * (fahrenheit - 32)
    celsjusz = round(celsjusz,2)
    print(f"Temp {fahrenheit} F to {celsjusz} st C")
    fahrenheit +=20

