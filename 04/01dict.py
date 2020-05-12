pair_list = [
    ["dzien dobry", "bonjour"],
    ["ziemniaki", "pomme de terre"],
    ["dziekuje", "merci"]
]

dict_fr = dict(pair_list)

print(dict_fr)
print(dict_fr['dziekuje'])

for k, v in dict_fr.items():
    print(f"{k} - translation: {v}")