# Задание 1
# Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def person(name, age, city):
    result = '{}, {} год(а), проживает в городе {}'.format(name, age, city)
    return result

print(person('Тарас', 33, 'СПб'))

# Задание 2
# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def max_of_3(numbers):
    print(max(numbers))

max_of_3([1, 20, 3])

# Задание 3
# Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# Теперь надо создать функцию attack(person1, person2).
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

# Ввод имен игроков
player_name = input('Введите имя героя: ')
enemy_name = input('Введите имя врага: ')

# Создание параметров игроков
player = {"name": player_name, "health" : 100, "damage" : 15, "armor": 1.5}
enemy = {"name": enemy_name, "health" : 100, "damage" : 50, "armor": 1.5}

# Функция для вычисления нанесенного урона
def result_damage(damage, armor):
    damage = int(damage/armor)
    return damage

# Функция, применяемая при атаке
def attack(person1, person2):
    person2["health"] -= result_damage(person1["damage"], person2["armor"])

# Одиночная атака и результат
attack(player, enemy)
print(enemy)