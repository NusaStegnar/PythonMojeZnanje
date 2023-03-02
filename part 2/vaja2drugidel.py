class PretvornikTemperature:

    def __init__(self):
        self.c_to_f(50)


    def c_to_f(self, temperatura):
        pretvorjena_temperatura = temperatura * 9 / 5 + 32
        print(f"{temperatura} stopinj Celzija je enako {pretvorjena_temperatura} Fahrnheit")

    def f_to_c(self, temperatura):
        druga_temperatura = (temperatura-32) * 5 / 9
        print(f"{temperatura} Fahrnheit je enako {druga_temperatura} stopinj Celzija")


pretvornik = PretvornikTemperature()
pretvornik.c_to_f(50)
pretvornik.f_to_c(83)
