# Задание 1
# Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран.
user_number = int(input('Введите число: '))

result = user_number + 2
print('Увеличенное на 2: ', result)

# Задание 2
# Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
user_number2 = int(input('Введите число: '))

while user_number2 < 0 or user_number2 > 10:
    print('Нужно ввести число от 0 до 10')
    user_number2 = int(input('Еще попытка: '))
else:
    result2 = user_number2**2
    print('Ваше число в квадрате: ', result2)

# Задание 3
# Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = int(input('Введите возраст: '))
weight = int(input('Введите вес: '))

if 50 < weight < 120:
    print(name, surname, ': Хорошее состояние')
else:
    if 30 < age < 40:
        print(name, surname, ': Требуется заняться собой')
    elif 40 < age:
        print(name, surname, ': Требуется обратиться к врачу')
    else:
        print('вам меньше 30, но вес плохой')