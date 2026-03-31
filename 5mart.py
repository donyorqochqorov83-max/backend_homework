# a = 20
# b = -30
# c =  a + b
# print(c)
#
#
# kvdrt_tmni = 20
# kvdrt_yuzi = kvdrt_tmni**2
# print(kvdrt_yuzi)
#
# a = -20
# b = 40
# c = b/a
# print(c)
#
# aholi_soni = 7_594_000_000
# print("Yer kurrasida", aholi_soni,"ga yaqin odam yashaydi")
#
#
# x,y,z = 10,-7.25,-30
# print(x,y,z)
# # type casting
# a = 10
# print(a)
# print(type(a))
# a = float(a)
# print(a)
# print(type(a))
# a = str(a)
# print(a)
# print(type(a))
#
# b = "Salom"
# print(b)
# print(type(b))
# b = "64692"
# b = int(b)
# print(b)
# print(type(b))
#
# c = 10.5
# print(c)
# print(type(c))
# # c = str(c)
# # print(c)
# # print(type(c))
# c = int(c)
# print(c)
# print(type(c))
#
# ism = 'Jonibek'
# yosh = 22
# xabar = ism + ' ' + str(yosh) + ' yoshda'
# print(xabar)
#
# ism = 'Jonibek'
# yosh = 22
# print(type(ism))
# print(type(yosh))
#
# t_yil = input("Tug'ilgan yilingizni kiriting: ")
# yosh = 2026 - int(t_yil)
# print("Siz " + str(yosh) + " yoshda ekansiz")


a = int(input("Istalgan sonni kiriting: "))
kvadrat =a**2
kub  =a**3
print(f"{a} ning kvadrati {kvadrat} ga teng")
print(f"{a} ning kubi {kub} ga teng")


yosh = int(input("Yoshingiz nechida? "))
t_yil = 2026 - yosh
print(f"Siz {t_yil} da tug'ilgansiz")

b = float(input("Birinchi sonni kiriting: "))
c = float(input("Ikkinchi sonni kiriting: "))
print(f"{b} + {c} = {b+c}")
print(f"{b} - {c} = {b-c}")
print(f"{b} * {c} = {b*c}")
print(f"{b} / {c} = {b/c}")