#vaja Razred bancni racun

class BancniRacun:
    def __init__(self, nosilec, stevilka, stanje):
        self.nosilec = nosilec
        self.stevilka = stevilka
        self.stanje = stanje

    def izpis(self):
        print("Obvestilo: stranka" , self.nosilec, self.stevilka, ". Novo stanje na tvojem racunu je" , self.stanje, "evrov.")

    def nakazi(self, vrednost):
        if self.stanje > vrednost:
            self.stanje -= vrednost
            print(self.stanje)
        else:
            print("Obvestilo: stranka", self.nosilec, self.stevilka, "Nimas dovolj denarja...")

mojracun = BancniRacun("Jaz", "Si5632178542", 165)
mojracun.nakazi(30)
mojracun.izpis()