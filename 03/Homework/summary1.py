"""Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string
rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście."""

friends = (input("Enter names of your closest friends, separated by a comma: "))
name_list = friends.split(",")
for step in name_list:
    print("Hello,", step)
