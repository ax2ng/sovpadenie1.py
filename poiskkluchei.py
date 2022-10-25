
def reverseLookup(slovar:dict, znachenie: str):
    spisokznachenii = []
    for i in slovar.keys():
        if slovar[i] == znachenie:
            spisokznachenii.append(i)
    return spisokznachenii


z = {'a': 'Одуванчик','b':'Одуванчик','c':'Одуванчик'}
x = {'d': 'Огурец','e':'Помидор'}
c = {'f': 'Подсолнух','g':'Подсолнух'}

print(reverseLookup(z,'Одуванчик'))
print(reverseLookup(x,'Помидор'))
print(reverseLookup(c,'Огурец'))

