# Создайте модуль.
# В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой функция должна вернуть None.
# Проверьте работу функций в этом же модуле.

import random

def get_random_element(list):
    if len(list) != 0:
        result = random.choice(list)
    else:
        result = "None"
    return result

my_list = [1, 2, 3, 4]

print(get_random_element(my_list))