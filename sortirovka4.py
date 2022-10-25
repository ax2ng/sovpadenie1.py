spisok = []

while (a := input('Введите число: ')) != '0':
    try:#проверка
        spisok.append(int(a))#добавление чисел
    except ValueError:
        ...
print(*sorted(spisok), sep='\r\n')#чтобы выводило на каждой новой строке