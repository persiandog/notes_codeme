class Ssak:
    pija_mleko = True
    kregoslup = True
    zmiennocieplne = True

    def __init__(self):
        print('zwierzęta należące do kręgowców')

class Czlowiek(Ssak):
    def __init__(self, imie, wiek, aktywny):
        self.imie = imie
        self.wiek = wiek
        self.aktywny = aktywny

c = Czlowiek('Adam', 30, True)
print(c.imie)