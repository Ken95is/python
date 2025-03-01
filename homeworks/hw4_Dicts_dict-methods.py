'Dicts'
#1

# day = {
#     '1': 'понедельник',
#     '2': 'вторник',
#     '3': 'среда',
#     '4': 'четверг',
#     '5': 'пятница',
#     '6': 'суббота',
#     '7': 'воскресенье'
# }
# print(day.get(input('Day: ')))

#2

# week = {'понедельник': 1, 'вторник': 2, 'среда' :3}
# print(week.get(input('Vvedite: '), 'Нет такого дня'))
# # print(week.get('среда'))
#3

# month = {
#     'January': 31,
#     'February': 28,
#     'April' : 30
# }

#4

# grades = {'математика': 5, 'физика': 4, 'химия': 3}
# poped_item = grades.popitem()
# grades2 = {'химия': 4}
# grades.update(grades2) #надо уточнить будет
# print(grades)

# grades = {'математика': 5, 'физика': 4, 'химия': 3}
# poped_item = grades.pop("химия")
# grades2 = {'химия': 4}
# grades.update(grades2)
# print(grades)

#5
# subjects = {'математика': 5, 'физика': 4, 'химия': 3}
# physics = subjects.pop('физика')
# print(subjects)

#6
# products = {'яблоки':50, 'бананы':30, 'апельсины':70}
# print(products.get(input('Название продукта: '), 'Товар отсутствует'))

#7
# config = {'theme':'dark', 'version':'1.0.1', 'debug': True}
# copy = config.copy() # метод copy()
# copy['debug'] = False
# print(config, copy)

# copy = dict(config) # функция dict()
# copy['debug'] = False
# print(config)
# print(copy)

# 8
# phonebook = {
#     'Иван': '123-45-67',
#     'Мария': '789-01-23',
#     'Олег': '456-78-90'
#     }
# print(phonebook.keys())

#9

# scores = {'Аня': 85, 'Борис': 92, 'Вика': 78,'Гена': 88}
# keys = list(scores.keys())
# values = list(scores.values())
# for keys in scores:
#     if keys[0] and values[0]:
#         print(keys, '-', values)

# 'не получается ни одним способом'

# items = list(scores.items())
# values = list(scores.values())
# for items in scores:
#     if items[0] and values[0]:
#         print(items, '-', values)
