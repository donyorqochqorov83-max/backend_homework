aka = {'ism':'axmedov islom','yosh':24,'t_yil':2000}
print(aka)
print(f"akamning ismi {aka['ism'].title()},{aka['t_yil']}-yilda tugilgan,{aka['yosh']} yoshda")

oila = {'dadam':'osh','oyim':'shashlik','akam':'somsa','singlim':'manti','men':'barak'}
print(f"Dadamning sevimli taomi {oila['dadam']}")
print(f"Oyimning sevimli taomi {oila['oyim']}")
print(f"Akamning sevimli taomi {oila['akam']}")
print(f"Singlimning sevimli taomi {oila['singlim']}")
print(f"Menning sevimli taomim {oila['men']}")

integer = "butun son"
float = "o'nlik son"
string = "matn"
for_ = "takrorlanuvchi amal"
if_ = "shart operatori"
else_ = "aks holda"
or_ = "yoki"
and_ = "va"
list_ = "ro'yxat"
dict_ = "lug'at"

formula = {'integer':"butun son",'float':"o'nlik son",'string':"matn",'for_':"takrorlanuvchi amal",'if_':"shart operatori",'else_':"aks holda",'or_':"yoki",'and_':"va",'list_':"ro'yxat", 'dict_':"lug'at"}
sd = input("Kalit so'z kiritng: ")
if sd in formula:
    print(f"{sd} ning ma'nosi {formula[sd]}")
else:
    print("Bunday so'z mavjud emas")

