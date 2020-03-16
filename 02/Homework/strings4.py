"""Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
Połącz dane w jeden ciąg book za pomocą spacji
Policz liczbę wszystkich znaków w napisie book"""

author = input("Who is your favourite writer?")
if author.isalpha():
    print("Author name entered correctly")
else:
    print("Please only use characters in author name")
    author = input("Who is your favourite writer?")
book = input("What's the title of your favourite book by that author?")
if book.isalpha():
    print("Book title entered correctly")
else:
    print("Please only use characters in book title")
    book = input("What's the title of your favourite book by that author?")
pages = input("how many pages does this book have?")
if pages.isdigit():
    print("Number of pages entered correctly")
else:
    print("Please only use digits in number of pages")
    pages = input("how many pages does this book have?")

print(author.title())
print(book.title())

print(author + " " + book + " " + pages)

print("The book title has ", len(book), " characters")
