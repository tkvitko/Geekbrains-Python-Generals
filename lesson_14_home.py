import math

# Задание 1
# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7, 8, 9]

result_list = [i for i in list1 if list2.count(i)]
print(result_list)

# Задание 2
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

# Элемент кратен 3
multiple_of_3 = [i for i in list if i%3 == 0]
print(multiple_of_3)

# Элемент положительный
positive = [i for i in list if i > 0]
print(positive)

# Элемент не кратен 4
not_multiple_of_4 = [i for i in list if i%4 != 0]
print(not_multiple_of_4)

# Задание 3
# Напишите функцию которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней чисел (если число положительное)
# и самих чисел (если число отрицательное) и возвращает результат (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

# Классический способ без генератора
def sqrt_if_positive(list):
    new_list = []
    for i in range(len(list)):
        new_list.append(math.sqrt(list[i])) if list[i] > 0 else new_list.append(list[i])
    return new_list

# Генератор и тернарный оператор в нем
def sqrt_if_positive2(list):
    new_list = [math.sqrt(number) if number > 0 else number for number in list]
    return new_list

print(list)
print(sqrt_if_positive(list))
print(sqrt_if_positive2(list))

# Задание 4
# Написать функцию которая принимает на вход число от 1 до 100.
# Если число равно 13, функция поднимает исключительную ситуации ValueError иначе возвращает введенное число, возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция.
# Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.

def my_func(number):
    if number != 13:
        result = number ** 2
    else:
        raise ValueError
    return result


user_number = int(input('Введите число: '))

try:
    result = my_func(user_number)
except ValueError:
    print('Исключение')
else:
    print(result)