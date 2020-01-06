# В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.
# Компьютер начинает его отгадывать предлагая игроку варианты чисел.
# Если компьютер угадал число, игрок выбирает “победа”.
# Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”.
# Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”.
# Игра продолжается до тех пор пока компьютер не отгадает число.

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