# Zadanie 8
#Ulepsz program z zadania 7, tak aby zwrócił ile banknotów
# 50, 20, 10 i 5 euro otrzyma użytkownik.

amount = float(input("How much money do you want to take on vacation (PLN)?"))
eur_rate = 4.2
usd_rate = 3.3

eur_amount = round(amount * eur_rate)
usd_amount = round(amount * usd_rate)

print("You can buy ", eur_amount, "Euro", "or ", usd_amount, "US dollars")

