class Vozilo:
    def __init__(self, znamka, model, moc, prostornina):
        self.znamka = znamka
        self.model = model
        self.moc = moc
        self.prostornina = prostornina

    def gre_na_avtocesto(sef):
        return True
    
class Traktor(Vozilo):
    def __init__(self, znamka, model, moc, prostornina):
        super(Traktor, self).__init__(znamka, model, moc, prostornina)

class Kombi(Vozilo):
    def __init__(self, znamka, model, moc, prostornina, prevaza_material):
        super(Kombi, self).__init__(znamka, model, moc, prostornina)
        self.prevaza_material = True


class OsebniAvto(Vozilo):
    def __init__(self, znamka, model, moc, prostornina, je_kabriolet):
        super(OsebniAvto, self).__init__(znamka, model, moc, prostornina)
        self.je_kabriolet = False

    def vozi_hitro(self):
        print("Lahko vozi hitro.")

traktor = Traktor("John Deer", " ", 400, 4.4)
print(traktor.znamka)

kombi = Kombi("Renaul", " ", 250, 1.9, True)
print(kombi.moc)
print(kombi.prevaza_material)
print(kombi.gre_na_avtocesto())

avto = OsebniAvto("BMW", "520", 177, 2.0, False)
avto.vozi_hitro()
print(avto.je_kabriolet)


