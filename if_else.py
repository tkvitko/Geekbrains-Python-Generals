value = int(input('Введите от 1 до 100'))
number = 23

if number == value:
    print('Угадали')
else:
    if value < number:
        print('Нужно больше')
    else:
        print('Нужно меньше')

#альтернативный if через тернайрный оператор
print ('Нужно больше' if value < number else 'Нужно меньше')