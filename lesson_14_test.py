def my_func(number):
# TBD  Почему не работает через тернарный оператор?
    result = number if number == 13 else number ** 2
#    if number != 13:
#        result = number ** 2
#    else:
#        raise ValueError
    return result