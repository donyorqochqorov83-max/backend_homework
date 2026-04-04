def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija *= son
    return natija

print(kopaytma(2, 4, 5)) 

def talaba_malumotlari(ism, familiya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar

talaba = talaba_malumotlari("Ali", "Valiyev", yosh=20, kurs=3, tuman="Yunusobod")
print(talaba)


def total_price(*narxlar, **kwargs):
    jami = sum(narxlar)
    discount = kwargs.get('discount', 0) 
    
    yakuniy_narx = jami * (1 - discount / 100)
    return yakuniy_narx

print(total_price(10000, 20000, 15000, discount=10))



def join_words(*sozlar, **kwargs):
    ajratuvchi = kwargs.get('sep', " ")
    return ajratuvchi.join(sozlar)

print(join_words("Python", "is", "awesome", sep="-"))
print(join_words("Salom", "Dunyo"))