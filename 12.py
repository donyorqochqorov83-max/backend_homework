def mijoz_malumotlari(ismi, familiyasi, t_yili, t_joyi, email=None, tel=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaradi."""
    mijoz = {
        'ism': ismi,
        'familiya': familiyasi,
        'tyil': t_yili,
        'yosh': 2026 - t_yili,
        'tjoy': t_joyi,
        'email': email,
        'telefon': tel
    }
    return mijoz

mijozlar = []
while True:
    print("\nMijoz ma'lumotlarini kiriting:")
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email (ixtiyoriy): ")
    tel = input("Telefon (ixtiyoriy): ")
    
    mijozlar.append(mijoz_malumotlari(ism, familiya, tyil, tjoy, email, tel))
    
    javob = input("Yana mijoz qo'shasizmi? (ha/yo'q): ")
    if javob.lower() != 'ha':
        break

for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}, "
          f"{mijoz['yosh']} yoshda, tel: {mijoz['telefon']}")
    

def kattasini_top(x, y, z):
    """Uchta sondan eng kattasini qaytaruvchi funksiya."""
    return max(x, y, z)

print(f"Eng kattasi: {kattasini_top(10, 25, 15)}")


def aylana_info(radius, pi=3.14159):
    """Aylana haqidagi ma'lumotlarni lug'atda qaytaradi."""
    aylana = {
        'radius': radius,
        'diametr': 2 * radius,
        'perimetr': 2 * pi * radius,
        'yuza': pi * (radius**2)
    }
    return aylana

print(aylana_info(5))


def tub_sonlar_top(min_son, max_son):
    tub_sonlar = []
    for n in range(min_son, max_son + 1):
        if n < 2:
            continue
        tub = True
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                tub = False
                break
        if tub:
            tub_sonlar.append(n)
    return tub_sonlar

print(f"Tub sonlar: {tub_sonlar_top(1, 20)}")


def fibonacci_gen(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1] + sonlar[x-2])
    return sonlar

miqdor = int(input("Nechta Fibonachchi soni kerak? "))
print(fibonacci_gen(miqdor))
