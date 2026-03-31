pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
for pochta in pochtalar:
    if "@" in pochta:
        print
    else:
        print("Noto'g'ri email: ",pochta)


parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]
maxsus_belgilar = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
for parol in parollar:
    if len(parol) < 8:
        print(f"{parol} Juda qisqa")
    
    elif not (any(char.isdigit() for char in parol) or any(char in maxsus_belgilar for char in parol)):
        print(f"{parol} Kuchsiz parol")
    
    else:
        print(f"{parol} Kuchli parol")



harorat = [20, 22, 19, 24, 25, 23, 21]

ortacha = sum(harorat) / len(harorat)
print(f"Haftalik o'rtacha harorat {ortacha}")

for sss in harorat:
    if sss > 22:
        print(f"{sss} - Iliq kun")
    else:
        print(f"{sss} - Salqin kun")


menyu = ["Osh", "Shashlik", "Manti", "Lag'mon"]
buyurtma = input('Nima buyurtma qilasiz? ')

topildi = False

for taom in menyu:
    if buyurtma.lower() == taom.lower():
        topildi = True
        break  
if topildi:
    print("Buyurtmangiz qabul qilindi")
else:
    print("Kechirasiz, bunday taom yo'q")

tahlil = [16, 21, 17, 30, 25]
for t in tahlil:
    if t >= 18:
        print("Xush kelibsiz")
    else:
        print("Yosh chegarasiga yetmagan")


xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
for xw in xabarlar:
    if xw == "Batareya past":
        print("Telefoningizni quvvatlang")


fayllar = ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]

musiqalar = []
rasmlar = []

for fayl in fayllar:
    if fayl.find(".jpg") != -1:
        rasmlar.append(fayl)
    
    elif fayl.find(".mp3") != -1:
        musiqalar.append(fayl)

print("Rasmlar ro'yxati:", rasmlar)
print("Musiqalar ro'yxati:", musiqalar)