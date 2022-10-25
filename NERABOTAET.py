
groupOne, groupTwo, groupThree = [], [], []
print('Введите число, чтобы остановить введите пустоту')
inpt = int(input())
while inpt == ' ':
    print('программа остановлена')
    exit()

    if inpt < 0:
        groupOne.append(inpt)
    elif inpt > 0:
        groupThree.append(inpt)
    else:
        groupTwo.append(inpt)
print(groupOne)
