class avto:
    def __init__(self, brend, model, rang, yil, korobka, narh):
        self.brend = brend
        self.model = model
        self.rang = rang
        self.yil = yil
        self.korobka = korobka
        self.narh = narh
        self.kilometr = 0 

    def get_info(self):
        return f"{self.brend} {self.model} {self.rang} {self.yil} {self.korobka} {self.narh}"

    def get_brend(self):
        return self.brend

    def get_model(self):
        return self.model

    def get_yil(self):
        return self.yil

    def get_narh(self):
        return self.narh

    def set_narh(self, narh):
        self.narh = narh

    def update_km(self, km):
        self.kilometr += km


avto1 = avto("GM", "Malibu", "Qora", 2024, "Avtomat", 40000)
avto2 = avto("BYD", "Song", "Oq", 2023, "Avtomat", 35000)

print(avto1.get_brend())
print(avto1.get_model())
print(avto1.get_yil())
avto1.set_narh(45000)
print(avto1.get_narh())
print(avto1.get_info())

class avtosalon:
    def __init__(self, salon_nomi, manzili):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.avtolar = []

    def add_avto(self, avto):
        self.avtolar.append(avto)

    def get_avtolar(self):
        return [mashina.get_info() for mashina in self.avtolar]


salon1 = avtosalon("GM Avto", "Toshkent")
salon1.add_avto(avto1)
salon1.add_avto(avto2)

print(salon1.salon_nomi)
print(salon1.get_avtolar())