
words = []
string = input('Введите слова: ')
words = string.split(' ')#сплит для разделения элементов, разделяет слова по пробелу
a = set(words)
print(a)