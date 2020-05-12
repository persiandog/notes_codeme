"""Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach."""

names_by_country = {'Poland': ['Susanna', 'Julia', 'Lena', 'Maja', 'Hannah', 'Sophia', 'Amelia', 'Alice', 'Alexandra', 'Natalie'],
                 'Germany': ['Mia', 'Emma', 'Hannah', 'Sophia', 'Anna', 'Emilia', 'Lina', 'Mary', 'Lena', 'Mila'],
                 'UK': ['Emily', 'Ella', 'Grace', 'Sophia', 'Olivia', 'Anna', 'Amelia', 'Aoife', 'Lucy', 'Ava'],
                 'Russia': ['Sophia', 'Mary', 'Anna', 'Anastasia', 'Victoria', 'Elizabeth', 'Polina', 'Alice', 'Daria', 'Alexandra'],
                 'Sweden': ['Alice', 'Lily', 'Maja', 'Elsa', 'Ella', 'Alice', 'Olivia', 'Julia', 'Ebba', 'Wilma'],
                 'Slovenia': ['Rosalia', 'Eva', 'Emma', 'Lara', 'Sarah', 'Masha', 'Mia', 'Anna', 'Agnes', 'Zoja'],
                 'Montenegro': ['Jelena', 'Milica', 'Marija', 'Ivana', 'Milena', 'Anna', 'Dragana', 'Radmila', 'Vesna', 'Ljiljana'],
                 'Malta': ['Helen', 'Julia', 'Emma', 'Elizabeth', 'Katherine', 'Maya', 'Leah', 'Emily', 'Amy', 'Mary'],
                 'Romania': ['Mary', 'Helen', 'Joanna', 'Andrea', 'Sophia', 'Alexandra', 'Antonia', 'Daria', 'Anna', 'Gabriella'],
                 'Portugal': ['Mary', 'Leonor', 'Matilda', 'Beatriz', 'Carolina', 'Mariana', 'Anna', 'Ines', 'Margaret', 'Sophia'],

}

names_compilation = []
popular_names = []

for i in names_by_country:
    names_compilation.extend(names_by_country[i])

for n in names_compilation:
    if names_compilation.count(n) >= 3:
        if n not in popular_names:
            popular_names.append(n)

print(popular_names)

