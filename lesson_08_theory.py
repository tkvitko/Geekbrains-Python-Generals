def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number): #если функция function вернула true
            result.append(number) #добавляем значение в список
    return result

#функция для проверки на четность
def is_even(number):
    return number % 2 == 0 #вернет true только для четного

#функция для проверки на нечетность
def is_not_even(number):
    return number % 2 != 0 #вернет true только для нечетного

#функция для проверки на "больше 4-х"
def is_greater_then_4(number):
    return number > 4 #вернет true только для "больше 4-х"

# Вводные
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Получение результатов через вспомогательные функции
print(my_filter(numbers, is_even))
print(my_filter(numbers, is_not_even))
print(my_filter(numbers, is_greater_then_4))

# Получение тех же результатов через lambda-функции
print(my_filter(numbers, lambda x: x % 2 == 0))
print(my_filter(numbers, lambda x: x % 2 != 0))
print(my_filter(numbers, lambda x: x > 4))