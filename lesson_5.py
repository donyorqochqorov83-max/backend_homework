cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'teala', 'audi']
cars.sort()
print(cars)

mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek', "O'tkirjon", 'Anvar', 'Bekzod']
print("sorted() qaytargan ro'yhat:",sorted(mehmonlar))
print("sorted() qaytargan ro'yhat:",sorted(mehmonlar, reverse=True))

print("Asl ro'yhat o'zgarmas qoldi:",mehmonlar)

ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))


fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
fruits.reverse()
print(fruits)

print(list(range(1,10)))
print(list(range(50,100)))

juft_sonlar = list(range(0,20,2))
toq_sonlar = list(range(1,20,2))
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)

narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narh ", arzon, ". Eng qimmat narh ", qimmat, ". Jami: ", jami)

cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'teala', 'audi']
ny_cars = cars[0:3]
a_cars = cars[2:5]
print(ny_cars)
print(a_cars)

print(cars[:4])
print(cars[2:])

sonlar = [1, 2, 3, 4, 5]
sonlar2 = sonlar[:]
sonlar2.append(6)
sonlar2.append(7)
print("Bu sonlar ro'yhati:", sonlar)
print("Bu sonlar2 ro'yhati:", sonlar2)

tomonlar = (20, 30, 55.2)
print(tomonlar)

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
toys = list(toys)
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys)
print(toys)

thisset = {"apple", "banana", "cherry",'cherry'}
print(thisset)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)