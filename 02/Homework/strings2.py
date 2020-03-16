"""Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy,
utwórz nowy łańcuch s3, dołączając s2 w środku s1."""

s1 = "word"
s2 = "word word"

s1_center = len(s1) // 2
s3 = s1[0:s1_center] + s2 + s1[s1_center:]

print(s3)