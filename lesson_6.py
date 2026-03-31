# mehmonlar = ['jonibek', 'Temurbek', 'Javlonbek', 'O\'tkirbek']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20-mart kuni oshga taklif qilamiz")
#     print("hurmat bilan, Palonchiyevlar oilasi")
#
# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")
#
# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
#
# print(sonlar)
# print(sonlar_kvadrati)
#
# dostlar = []
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-do'stingizni kiriting: "))
# print(dostlar)

# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())
#
# ism  = input('Ismingiz nima?\n>>>')
# if ism.lower() != 'ali':
#     print(f"Uzr, {ism.title()} biz Alini kutayapmiz.")
# else:
#     print("Salom, Ali")
#
# javob = float(input("12x6 nechiga teng?>>>"))
# if javob!=72:
#     print("Javob xato!")
# else:
#     print("Javob to'g'ri")
#
# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>=18:
#     print('Xush kelibsiz!')
# else:
#     print('Kirish mumkin emas!')
#
# login = input("Yangi login tanlang: ")
# if len(login)<=5:
#     print("Login 5 harfdan ko'proq bo'lishi shart!")
#
# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2026-yil<18:
#     print(f"Yoshingiz {2026-yil}da ekan.")
#     print("Kirish mumkin emas")
# else:
#     print("Xush kelibsiz!")
#
# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

# x, y = 55, 50
# print("x>y") if x>y else print("x<y")

foydalanuvchilar=['Jalol','Suhrob','Atham','Sardor','Dilshod']
foydalanuvchi = input("Yangi login tanlang: ")
if foydalanuvchi in foydalanuvchilar:
    print("Login band, iltimos boshqa login tanlang!")
else:
    print("Xush kelibsiz !")

sonlar = int(input("Istalgan butun son kiriting: "))
for n in range(2, 11):
    if sonlar % n == 0:
        print(f"{sonlar} soni {n} ga qoldiqsiz bo'linadi")
juft_son=int(input("Juft son kiriting: "))
if juft_son % 2 ==0 :
    print("Raxmat!")
else:
    print("Bu son juft emas ")

yosh = int(input("Yoshingizni kiriting: "))
if yosh <= 4 or yosh >=60:
    print("Sizga kirish bepul")
elif yosh < 18:
    print("Siz uchun bilet narxi 10.000 so'm")
else:
    print("Siz uchun bilet narxi 20.000 so'm")

son_1 = float(input("Birinchi sonni kiriting: "))
son_2 = float(input("Ikkinchi sonni kiriting: "))
if son_1 < son_2:
    print(f"{son_1}<{son_2} ")
elif son_1 > son_2:
    print(f"{son_1}>{son_2} ")
else:
    print(f"{son_1}={son_2} ")