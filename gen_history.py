import random

out_path = input('Введите имя файла (без расширения): ')

count = int(input('Введите количество строк: '))

for i in range(count):
    with open(f'{out_path}.txt', 'a', encoding='UTF-8') as f:
        f.write(f"N: {random.choice(['do', 'do_dies', 're', 're_dies', 'mi', 'fa', 'fa_dies', 'sol',
                'sol_dies', 'la', 'la_dies', 'si', 'do2'])}; P: {random.randint(1, 1000)} m\n")

