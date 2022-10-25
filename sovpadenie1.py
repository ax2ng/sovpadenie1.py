from random import randint


spisok = []  #Обозначение переменных
slovar = {}
n = int(input('Введите количество кортежей: ')) # n - количество кортежей в массиве
for i in range(n):
    a = (randint(1, 100), randint(1, 100)) #Создаем кортежи из случайных целых чисел
    spisok.append(a)#Вносим кортежи в массив
for i in range(n):
    for j in range(0, 2):
        if spisok[i][j] in slovar.keys():
            slovar[spisok[i][j]] += 1
        else:
            slovar[spisok[i][j]] = 1
print(*spisok)
print(max(slovar.values()))

