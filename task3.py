def god():
    year = int(input('Введите год : '))
    if year % 4!=0:
        return('невисокосный год')
    else:
        return('високосный год')
print(god())