# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

amount = float(input("How much money do you want to take on vacation (PLN)?"))
eur_rate = 4.2
usd_rate = 3.3

eur_amount = round(amount * eur_rate)
usd_amount = round(amount * usd_rate)

print("You can buy ", eur_amount, "Euro", "or ", usd_amount, "US dollars")
