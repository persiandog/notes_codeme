import random
"""Napisz grę - kamień (k) / papier (p) / nożyce (n).
Użytkownik podaje jedną z 3 figur.
Komputer losuje jedną z 3 figur.
Sprawdź kto wygrał tę rundę.
Zmień kod tak, by użytkownik mógł podac liczbę rund.
Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’"""

options = ['rock', 'paper', 'scissors']
cpu = random.choice(options)

rounds = int(input("How many rounds do you want to play? "))
cpu_score = 0
user_score = 0
user = False

while user == False and rounds > 0:
    user = input("Enter one: rock, paper or scissors: ")
    if user == 'rock' or 'paper' or 'scissors':
        print("The computer has drawn %s and you have drawn %s " % (cpu, user))
        rounds = rounds - 1
    if user == "rock":
        if cpu == "rock":
            cpu_score = cpu_score + 1
            user_score = user_score + 1
            print("Tie! Scores: Computer ", cpu_score, ", you ", user_score)
        elif cpu == "paper":
            cpu_score = cpu_score + 1
            user_score = user_score + 0
            print("Computer wins! Scores: Computer ", cpu_score, ", you ", user_score)
        else:
            cpu_score = cpu_score + 0
            user_score = user_score + 1
            print("You win! Scores: Computer ", cpu_score, ", you ", user_score)
    if user == 'paper':
        if cpu == 'rock':
            cpu_score = cpu_score + 0
            user_score = user_score + 1
            print("You win! Scores: Computer ", cpu_score, ", you ", user_score)
        elif cpu == 'paper':
            cpu_score = cpu_score + 1
            user_score = user_score + 1
            print("Tie! Scores: Computer ", cpu_score, ", you ", user_score)
        else:
            cpu_score = cpu_score + 1
            user_score = user_score + 0
            print("Computer wins! Scores: Computer ", cpu_score, ", you ", user_score)
    if user == "scissors":
        if cpu == "rock":
            cpu_score = cpu_score + 1
            user_score = user_score + 0
            print("Computer wins! Scores: Computer ", cpu_score, ", you ", user_score)
        elif cpu == "paper":
            cpu_score = cpu_score + 0
            user_score = user_score + 1
            print("You win! Scores: Computer ", cpu_score, ", you ", user_score)
        else:
            cpu_score = cpu_score + 1
            user_score = user_score + 1
            print("Tie! Scores: Computer ", cpu_score, ", you ", user_score)

    user = False
    cpu = random.choice(options)
    finish_cmd = input("When you get tired, type 'finish' here. To continue, hit enter key: ")
    if finish_cmd == "finish":
        print("The end. Thank you!")
        break