from datetime import datetime, date

z = {}
n = int(input('polzovateli'))
for i in range(n):
    firstName = input('familii')
    bDate = input('data')
    email = input('email')
    z[firstName] = [bDate, email]

x = input('data')
dateCheck = datetime(int(x.split(',')[-1]), int(x.split(',')[1]), int(x.split(',')[0]))
for i in z.keys():
    print(list(z[i])[0])
    if datetime(int(list(z[i])[0].split(',')[-1]), int(list(z[i])[0].split(',')[1]),
                     int(list(z[i])[0].split(',')[0])) > dateCheck:
        print(f'{i}- proverka proidena')

