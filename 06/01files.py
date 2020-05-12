""" Utwórz plik na pulpicie zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć
w nowej linii. Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś.
- zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami
- plik z cytatami powinen również zawierać informację o autorze, wyświetl cytat i pod spodem autora"""

import os
import random

def show_quote(text):
    random_quote = random.choice(quotes)
    random_quote = random_quote.split('.')
    print('*' * 70)
    print(random_quote[0].center(70))
    print("*" * 70)

#filename = input("Enter file name: ")
filename = 'quotes.txt'
if os.path.exists(filename) and os.stat(filename).st_size > 0:
    with open(filename) as fopen:
        quotes = fopen.readlines()
else:
    print("No quotes to show")

show_quote(quotes)




