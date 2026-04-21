import datetime as dt

bugun = dt.datetime.now()
for i in range(10):
    sana = bugun + dt.timedelta(weeks=2 * i)
    print(sana.strftime("%Y-%m-%d"))

ramazon_hayiti = dt.datetime(2026, 3, 20)
qurbon_hayiti = dt.datetime(2026, 5, 27)
bugun = dt.datetime.now()

ramazon_farq = bugun - ramazon_hayiti
qurbon_farq = qurbon_hayiti - bugun

print(f"Ramazondan {ramazon_farq.days} kun o'tdi.")
print(f"Qurbon hayitiga {qurbon_farq.days} kun qoldi.")

bugun = dt.datetime.now()
birthday = dt.datetime(2027,3,31)
farq = birthday - bugun
print(farq)
print(f"Tug'ilgan kungacha{farq.days} kun qoldi")

import re

tel_raqam = input("Telefon raqamingizni kiriting (+998XXXXXXXXX): ")
andoza = r"^[\+]998\d{9}$"

if re.match(andoza, tel_raqam):
    print("Raqam to'g'ri kiritildi.")
else:
    print("Xato format! Namuna: +998901234567")

def link_ajratuvchi(matn):
    andoza = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
    linklar = re.findall(andoza, matn)
    return linklar

matn = "Mening saytim https://google.com va yana biri http://kun.uz sahifasi."
print(link_ajratuvchi(matn))