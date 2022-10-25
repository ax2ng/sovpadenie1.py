print('Введите строку')

stroka = input()
try:
    x = int(stroka)
    if int(x) in range (1):
        print('Введите строку')
        stroka = input()
    elif stroka == ' ':
        print('Введите строку')
        stroka = input()

    y = []
    for i in stroka:
        y.append(i)
    z = set(y)
    print('Количество уникальных символов в строке ' +stroka+' = '+str(len(z)))
except:
    if len(stroka) != 0:
        y = []
        for i in stroka:
            y.append(i)
        z = set(y)
        print('Количество уникальных символов в строке ' +stroka+' = '+str(len(z)))

    else:
        print('Введите заполненную строку')
        stroka = input()
        y = []
        for i in stroka:
            y.append(i)
        z = set(y)
        print('Количество уникальных символов в строке ' +stroka+' = '+str(len(z)))