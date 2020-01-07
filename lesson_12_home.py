import json
import pickle

# Исходные данные
my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито','year': 2014}]}

# конвертация объекта в JSON
print(json.dumps(my_favourite_group))

# конвертация объекта в байты
print(pickle.dumps(my_favourite_group))

# запись объекта как JSON в файл
with open('file.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

# запись объекта как байты в файл
with open('file.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)

# чтение JSON из файла как объект
with open('file.json', 'r', encoding='utf-8') as f:
    result_from_json = json.load(f)

print(result_from_json)

# чтение байт из файла как объект
with open('file.pickle', 'rb') as f:
    result_from_pickle = pickle.load(f)

print(result_from_pickle)