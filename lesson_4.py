mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
narhlar = [12000, 18000, 10900, 22000]
sonlar = ["bir", 'ikki', 3, 4, 5]
ismlar = []

print(mevalar)
print(narhlar)
print(sonlar)
print(type(mevalar))

print("Birinchi meva: ", mevalar[0].title())
print("ikkinchi meva: ", mevalar[1].upper())

narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000
narhlar[2] = 11000
narhlar[3]= narhlar[3]+2000
print(narhlar)

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("tarvuz")
print(mevalar)

cars = []
cars.append("Lacetti")
cars.append("Nexia 3")
cars.append("Cobalt")
print(cars)

cars = ["Lacetti", "Nexia 3", "Cobalt"]
cars.insert(0,'Malibu')
print(cars)
cars.insert(2,'Damas')
print(cars)

del mevalar[1]
print(mevalar)
mevalar.remove('shaftoli')
print(mevalar)

hayvonlar = ['it', 'mushuk', 'sigir', 'qoy', 'quyon', 'mushuk']
hayvonlar.remove('mushuk')
print(hayvonlar)

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot =bozorlik.pop(3)
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)