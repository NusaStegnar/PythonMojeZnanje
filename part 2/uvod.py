#vaja2delTecaja

class Avto:
    def __init__(self, znamka, model, prostornina, moc):
        self.znamka = znamka
        self.model = model
        self.prostornina = prostornina
        self.moc = moc
        
    def __str__(self):
        return f"Znamka: {self.znamka} Model: {self.model}" 
    
    def __repr__(self):
        return f"Znamka: {self.znamka} Model: {self.model}" 

avto1 = Avto("Ford", "Focus", 1.6, 113)
print(avto1.znamka, avto1.model, avto1.prostornina, avto1.moc)

""" avto1.znamka = "Audi"
print(avto1.znamka) """


avto2 = Avto("BMW", "520", 2.0, 177)
print(avto2.znamka, avto2.model, avto2.prostornina, avto2.moc) 

avto3 = Avto("VW", "Golf", 1.8, 157)
print(avto3.znamka, avto3.model, avto3.prostornina, avto3.moc) 

seznam_vozil = [avto1, avto2, avto3]
print(seznam_vozil)

seznam_vozil.sort(key=lambda x: x.moc)

print(seznam_vozil)

print(f"Najmocnejsi avto je: {seznam_vozil[-1]}.")
