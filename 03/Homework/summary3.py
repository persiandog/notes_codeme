"""W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery,
wielkie litery, cyfry i znaki specjalne."""

txt = input("Enter your birthday and birth place: ")

print("Capital Letters: ", sum(1 for c in txt if c.isupper()))
print("Lowercase Letters: ", sum(1 for c in txt if c.islower()))
print("Digits: ", sum(1 for c in txt if c.isdigit()))

# needs work:
#special_chars = [#, $, %, ^, &, *, ., ', :]
#print("Special characters: ", sum(1 for c if any c in speial_chars))