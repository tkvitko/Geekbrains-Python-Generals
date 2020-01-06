import random

# Начальные значения диапазона
min = 1
max = 100

print(f'Загадайте число от {min} до {max}')
solution = None

while solution != '=':
    number = random.randint(min, max)
    print(number)
    solution = input('Это больше, меньше и равно загаданному?')
    # если взятое число меньше загаданного
    if solution == '<':
        # сдвигаем левый край диапазона
        min = number + 1
    # если взятое число больше загаданного
    else:
        # сдвигаем правый край диапазона
        max = number - 1

print(f'Конец игры, число было {number}')