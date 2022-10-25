spisok = []

while (a := input('Введите число: ')) != '0':
    try:
        spisok.append(int(a))
    except ValueError:
        ...
spisok.sort(reverse=True)#для того, чтобы сделать обратно
print(*(spisok), sep='\r\n')#звездочка, чтобы убрать скобки списка