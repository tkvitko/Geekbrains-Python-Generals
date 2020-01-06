#  Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
#  В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
#  Затем создайте вторую функцию удаляющую эти папки.
#  Проверьте работу функций в этом же модуле.

import sys, os

def create_structure():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), '{}_{}'.format(sys.platform, i))
        print('+', path)
#        os.mkdir(path)

create_structure()

def delete_structure():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), '{}_{}'.format(sys.platform, i))
        print('-', path)
#        os.remove(path)

delete_structure()