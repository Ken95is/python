'=============================Встроенные функции=============================='
# map, filter, reduce, zip, enumerate

# zip - соединяет несколько последовательностей (получаем генератор, в котором элементы - tuple)

# list1 = [1,2,3,4,5]
# list2 = ['a', 'b', 'c']
# list3 = [0.1, 5.5, 10.8, 0.5]

# zipped = zip(list1, list2, list3)
# print(list(zipped))
# for i in zipped:
#     print(i)


# enumerate - нумерует последовательность (по дефолту с 0) (тоже получаем генератор)

# enum = enumerate('hello', 45)
# # print(list(enum))

# for i in enum:   # цикл
#     print(i)

# for num, elem in enum:  # множественное присвоение
#     print(num, elem)


# map - принимает другую функцию и последовательность (записывает в новую последовательность результат функции,
# в которую передаются элементы последовательности)

# list_ = ['1', '2', '3', '4']
# mapped = map(int, list_)  #(1,2,3,4)
# print(list(mapped))

# def func_(x):
#     return x ** 2

# list_1 = [3, 1, 2, 5]

# mapped = list(map(func_, list_1))'3', '4']
# mapped = map(int, list_)  #(1,2,3,4)
# print(list(mapped))

# def func_(x):
#     return x ** 2
# print(mapped)

# print(list(map(lambda x: x ** 2, [1,2,3])))


# filter - возвращает генератор, с элементами прошедшими фильтрацию(какое-то условие), принимает функцию и последовательность

# list1 = ['hello', 'hi', '123', '3']
# filtered = filter(str.isdigit, list1)  #('123', '3')
# print(list(filtered))

# print(list(filter(lambda x: x > 0, [23, -3, 2, -5, 0])))

'---------------------------------------------------------------------------------------------------'
# reduce - принимает функцию и последовательность, возвращает 1 результат (передаваемая функция должна принимать 2 аргумента)

from functools import reduce

# print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))

# print(reduce(lambda x, y: x + y, ['hi', 'D', 'A', 'hello']))   #hiDAhello


'-----------------------------------Задачи----------------------------------------'

# ZIP

# list1 = [1,2,3,4]
# list2 = ['a', 'b', 'c', 'd']

# # Возведите во вторую степень числа из list1
# # Сделайте строки верхним регистром в list2
# # Сделайте dict при помощи zip и этих двух листов

# mapped1 = list(map(lambda x: x ** 2, list1))
# mapped2 = list(map(str.upper, list2))
# dict1 = dict(zip(mapped1, mapped2))
# print(dict1)


# list1 = [1,2,3,4]
# list2 = [10 ,20 ,30 ,40]

# list3 = list(zip(list1, list2))
# # [(1, 10), (2, 20), ...]

# mapped = list(map(lambda x: x[0] + x[1], list3))
# print(mapped)

'----------------------------------------------------------------------------'
# list1 = [1, 2, 3, 4, 5]  
# list2 = [1, 3, 3, 0, 5]

# zipped = zip(list1, list2)
# print(list(map(lambda x: x[0] == x[1], zipped)))

# print(list(map(lambda x: x[0] == x[1], zip(list1, list2))))
# print(list(map(lambda x, y: x == y, list1, list2)))
'---------------------------------------------------------------------'

# FILTER

# print(list(filter(lambda x: len(x) > 5, ['hi', 'hello', 'master'])))

# list1 = ['hello', 'яблоко', 'Облако', 'блок']
# print(list(filter(lambda x: x[0].lower() in 'аеёюиуоэя', list1)))


# list1 = ['шалаш', 'мам', 'арора']
# list2 = filter(lambda x: x == x[::-1], list1)
# print(list(list2))


# reduced = (reduce(lambda x, y: x*y,[12, 2, 3, 4]))
# print(reduced)
# print(reduce(lambda x, y: x*y,[12, 2, 3, 4]))

print(reduce(lambda x, y: x + ',' + y, ['hi', 'D', 'A', 'hello']))
