'''
print("Tip 1:\t\t" , type(1))
print("tip 1.0:\t" , type(1.0))
print("tip 'blabla':\t" , type("blabla"))
print("Tip[1, 2, 3]:\t", type([1, 2, 3]))


class Kaca:
    pass

kaca = Kaca()
print(kaca)



#damo se atribute

class Kaca:
    ime = "python"

kaca = Kaca()
print(kaca.ime)


#damo se atribute

class Kaca:
    ime = "python"

    def spremeni_ime(self, novo_ime):
        self.ime = novo_ime

kaca = Kaca()
print(kaca.ime)

kaca.spremeni_ime("anakonda")
print(kaca.ime)



#class Kaca se drugace

class Kaca:

    def __init__(self, ime):
        self.ime = ime

    def spremeni_ime(self, novo_ime):
        self.ime = novo_ime
python = Kaca("python")
anakonda = Kaca ("anakonda")

print(python.ime)
print(anakonda.ime)



#_______________________________________
#razred Vozilo

class Vozilo:
    def __init__(self, tip, st_koles, st_sedezev, prostornina, moc):
        self.tip = tip
        self.st_koles = st_koles
        self.st_sedezev = st_sedezev
        self.prostornina = prostornina
        self.moc = moc

    def __str__(self):
        return f"Jaz sem vozilo tip {self.tip}, vozim se na {self.st_koles} kolesih in sprejmem {self.st_sedezev} potnika. Pri prostornini {self.prostornina} ccm zgeneriram {self.moc} konjev."
        
sportni = Vozilo("sportni", 4, 2, 3000, 300)
print(sportni)


#Nadgradnja razreda Vozilo

class Vozilo:
    def __init__(self, tip, st_koles, st_sedezev, prostornina, moc):
        self.tip = tip
        self.st_koles = st_koles
        self.st_sedezev = st_sedezev
        self.prostornina = prostornina
        self.moc = moc

        #druge lastnosti
        self.trenutno_v_vozilu = 0

    def __str__(self):
        return f"Jaz sem vozilo tip {self.tip}, vozim se na {self.st_koles} kolesih in sprejmem {self.st_sedezev} potnika. Pri prostornini {self.prostornina} ccm zgeneriram {self.moc} konjev."

    
    def vstop_potnika(self, koliko=1):
        if self.trenutno_v_vozilu + koliko > self.st_sedezev:
            print("Ni dovolj sedezev!")
        else:
            self.trenutno_v_vozilu += koliko
            print(f"Dodanih {koliko} potnikov. Trenutno je v vozilu {self.trenutno_v_vozilu} potnikov.")

    def odpelji(self):
        if self.trenutno_v_vozilu == 0:
            print("Ne morem odpeljati, ni voznika!")
        else:
            print(f"Vrum, vrum! odpeljal sem {self.trenutno_v_vozilu} potnikov.")

sportni = Vozilo("sportni", 4, 2, 3000, 300)
sportni.odpelji()
sportni.vstop_potnika()
sportni.odpelji()
sportni.vstop_potnika(2)
'''

#Povezovanje na bazo

class DatabaseManager:
    def __init__(self, host, ime_baze, user, password):
        self.host = host
        self.ime_baze = ime_baze
        self.user = user
        self.password = password

        print("Baza kreirana")

    def connect(self):
        print(f"Povezava na bazo {self.ime_baze} uspesna!")

    def poizvedba (self, query):
        #najprej se povezemo na bazo
        self.connect()

    def disconnect(self):
        print(f"Uspesno ste prekinili povezavo z bazo {self.ime_baze}!")

        #implementacija
        print(f"Uspesno ste na bazi {self.ime_baze} izvedli poizvedbo {'query'}.")
        resp = {"status": 5, "data": {"title": "Python poizvedba"}, "body": "To so simulirani podatki iz baze!"}
        return resp
    
db = DatabaseManager("127.0.0.1", "moja_baza", "Nusa", "Wh57Vsa@")
podatki = db.poizvedba("SELECT * PROM znanje_programiranja")

print("Naslov: {podatki['data']['title']}")
print("Besedilo: {podatki['data']['body']}")
db.disconnect

    
        

        
