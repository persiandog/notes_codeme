"""Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą
literę i mieć długość conajmniej 8 znaków. Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
 Wyświetl różne komunikaty w zależności od rodzaju błędu."""

password = input("Please provide your password: ")
check_alpha = password.isalnum()
check_num = False
for character in password:
    if character.isdigit():
        check_num = True
check_upper = False
for character in password:
    if character.isupper():
        check_upper = True
check_len = len(password) >= 8

if check_alpha == False:
    print("Incorrect password. Your password lacks letters")
elif check_num == False:
    print("Incorrect password. Your password lacks digits")
elif check_upper == False:
    print("Incorrect password. Your password should contain at least 1 uppercase letter")
elif check_len == False:
    print("Incorrect password. Your password should contain at least 8 characters")
else:
    print("Thank you, password ok")