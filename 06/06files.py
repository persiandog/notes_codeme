"""Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych. Sprawdź dla każdej kart jej typ.
Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt."""



def is_card_number(number):
    return number.isdecimal() and len(number) in [13, 15, 16]

def starts_with_correct_digits(number):
    if 51 <= int(number[0:2]) <= 55:
        return True
    elif 2221 <= int(number[0:4]) <= 2720:
        return True
    else:
        return False

def show_card_type(number):
    if len(number) in [13, 16] and number[0] == '4':
        print("This is a visa card")
        save_to_file('visa.txt', number)

    elif len(number) == 16 and starts_with_correct_digits(number):
        print("This is a MasterCard")
        save_to_file('mastercard.txt', number)

    elif len(number) == 15 and (number[0:2] in ['34', '37']):
        print("This is American Express")
        save_to_file('american express.txt', number)


    else:
        print("Unknown card")
        save_to_file('other.txt', number)

def save_to_file(filename, number):
    with open(filename, 'a') as fp:
        fp.write(f"{number}\n")

with open('cards.txt') as fopen:
    cards = fopen.read()
    cards = cards.split()

for nr_card in cards:
    nr_card = nr_card.replace(" ", "")
    print("Entered number: ", nr_card)

    if is_card_number(nr_card):
        show_card_type(nr_card)
    else:
        print("This is not a card number")