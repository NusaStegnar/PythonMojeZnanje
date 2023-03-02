import random

class Karta:
    def __init__(self, barva, vrednost):
        self.barva = barva
        self.vrednost = vrednost

    def __repr__(self):
        return f"{self.barva} {self.vrednost}"

    def __str__(self):
        return f"{self.barva} {self.vrednost}"
    
class Igralec:
    def __init__(self, ime):
        self.ime = ime
        self.karta_v_roki = []

    def __str__(self):
        return f"{self.ime}"
    
    def sprejmi_karte(self):
        self.karta_v_roki.append(karta)

    def pokazi_karte(self):
        print(self.ime)
        for karta in self.karta_v_roki:
print(karta)
print()
    

class Kup:
    def __init__(self, seznam_kart):
        self.seznam_kart = seznam_kart
        self.premesaj_karte(10)

    def premesaj_karte(self, n):
        for i in range (10):
            random.shuffle(self.seznam_kart)

    def deli_karto(self):
        return self.seznam_kart.pop()    
  

barve = ['Srce', 'Kara', 'Pik', 'Kriz']
vrednosti = ['As', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Fant', 'Kraljica', 'Kralj']

karte = []

for barva in barve:
    for vrednost in vrednosti:
        karta = Karta(barva=barva, vrednost=vrednost)
        print(karta)
        karte.append(karta)

kup = Kup(seznam_kart=karte)




igralec1 = Igralec ("Maja")
igralec2 = Igralec ("Janez")
igralec3 = Igralec ("Ana")
igralec4 = Igralec ("Matej")

seznam_igralcev = [igralec1, igralec2, igralec3, igralec4]

for i in range (6):
    for igralec in seznam_igralcev:
        karta = kup.deli_karto()
        igralec.sprejmi_karte(karta)

for igralec in seznam_igralcev:
    igralec.pokazi_karte()