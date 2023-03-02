class OsnovniValidator:
    def __init__(self,podatki):
        self.podatki = podatki
        self.validacija_uspesna = False
        self.preveri_prisotnost()
        self.preveri_vsebino()


    def preveri_prisotnost(self):
        if not self.podatki.get("ime", None):
            raise Exception("Ime ni prisotno.")
        
        if not self.podatki.get("starost", None):
            raise Exception("Starost ni prisotna.")
        
        if not self.podatki.get("kraj_bivanja", None):
            raise Exception("Kraj bivanja ni prisoten.")
        
        print("Vsi podatki prisotni.")

    
    def preveri_vsebino(self):
        if not type(self.podatki.get("ime")) == str:
            raise Exception ("Ime ni tipa string.")
        
        if not type(self.podatki.get("starost")) == int:
            raise Exception ("Starost ni tipa integer.")
        
        if not type(self.podatki.get("kraj_bivanja")) == str:
            raise Exception ("Kraj bivanja ni tipa string.")
        
        print("Vsebina pravilna.")


class RazsirjeniValidator(OsnovniValidator):
    def __init__(self, podatki):
        super(RazsirjeniValidator, self).__init__(podatki)
        self.preveri_starost()
        self.preveri_kraj_bivanja()
        self.validacija_uspesna = True

    def preveri_starost(self):
        starost = self.podatki.get("starost")
        if starost < 18:
            raise Exception("Oseba je mmladoletna.")
        
    def preveri_kraj_bivanja(self):
        kraj_bivanja = self.podatki.get("kraj_bivanja")
        if not kraj_bivanja in ["Ljubljaan", "Kranj"]:
            raise Exception("Nepravilen kraj.")
        
        
        
        
        
podatki = {
    "ime" :"Janez",
    "starost" : 21,
    "kraj_bivanja" : "Ljubljana" 
}

#validator = OsnovniValidator(podatki)
validator = RazsirjeniValidator(podatki)