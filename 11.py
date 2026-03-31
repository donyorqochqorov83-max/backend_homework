# ismlar = []
#
# print("Yaqin do'stlaringizni ro'yhatini tuzamiz.")
# n=1
# while True:
#     savol = f"{n}-do'stingizni ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
#
# print("Do'stlaringiz ro'yhati:")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringiz yoshinin saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
#
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob =='no':
#         ishora = False
#
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)

# talabalar  = ['jonibek',' husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi.")
#     baholangan_talabalar[talaba] = baho

# print(talabalar)





# while True:
#     svetafor = input("Svetafor qaysi rangda? ")
#     if svetafor in ('qizil','sariq','yashil'):
#         print("raxmat to'g'ri keladi")
#         break
#     else:
#         continue

# import random

# tasodifiy_son = random.randint(1, 10)

# print("1 dan 10 gacha bo'lgan sonni toping.")

# while True:
#     taxmin = int(input("Soningizni kiriting: "))

#     if taxmin == tasodifiy_son:
#         print("Tabriklaymiz, siz topdingiz!")
#     else:
#         print("Noto'g'ri, qayta urinib ko'ring")


dostlar = []

print("Do'stlaringiz ismlarini kiriting (to'xtatish uchun 'stop' deb yozing):")
while True:
    ism = input("Ism kiriting: ")
    
    if ism.lower() == 'stop':
        break
    
    dostlar.append(ism)

print("Sizning do'stlaringiz ro'yxati:")
for d in dostlar:
    print(d.title())