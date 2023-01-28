import itertools

text = input('Введи текст:\n')
data = input('Введи данные через пробел:\n').split()

combin = itertools.permutations(data)

with open('combinations.txt', 'w') as file:
    for i in combin:
        file.write(f'{text}: ')
        for j in i:
            file.write(j)
        file.write('\n')


