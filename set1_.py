'=========================================Set================================================'
# set - это изменяемый, неупорядоченный, неиндексируемый, итерируемый тип данных, который хранит в себе уникальные значения,
#  так же только элементы, которые являются неизменяемыми типами данных

# list1 = [12, 'hi', [1,2,3], None, True, False, {'a':1, 'b': 2}]

# set1 = {12, 'hi', 'a', 'hello'}

# set1 = {1, 0, "hi", 'hello', 2, 3, True, 1, False}
# print(set1)

# print(dir(set))

# for i in set1:
#     print(i)

'==================================FIFO - LIFO====================================='

# FIFO - first in first out
# LIFO - last in first out

'================================Методы==================================='
# print(dir(set))

# add - добавляет элемент в set

# set1 = {3, 'hi', True}
# set1.add(4)
# print(set1)

# pop - удаяляет элемент случайно

# set2 = {True, 'hello', 'hi'}
# set2.pop()
# print(set2)

# remove - удаляет элемент по значению

# set3 = {1, 'hello', 'hi'}
# set3.remove('hi')
# print(set3)

# update - расширяет сет
# set4 = {1,2,3}
# set5 = {3,5,6}
# set4.update(set5)
# print(set4)

# difference - находит разницу в сетах (разность множеств)

# set6 = {1,2,3}
# set7 = {3,4,5}

# print(set6.difference(set7))  # {1,2}
# print(set7.difference(set6))  # {4,5}

# a = set()
# print(type(a))

# list_1 = [1,2,3, 'hi']
# str1 = 'abc'
# set2 = set(str1)
# print(set2)

# my_set = set([1, 2, 3, 4]) - создание множества с помощью функции set()

# discard - удаление элемента

# union(),| - обьединение множеств

# intersection(),& - пересечение множеств, операция которая возврщает элементы присутствующие в обоих множествах(находит
# общие элементы между двумя и более наборами данных)
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# intersection = set1 & set2 # {3, 4}
# print(intersection)
'----------------------------------------------'

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# intersection = set1.intersection(set2) # {3, 4}
# print(intersection)
'----------------------------------------------'
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {4, 5, 6, 7}
# intersection = set1.intersection(set2, set3)
# print(intersection)  # {4}

# # Или с использованием оператора '&'
# intersection = set1 & set2 & set3
# print(intersection)  # {4}
'------------------------------------------------'
# symmetric_difference(),^ - симметрическая разность


'======================================Tuple====================================='
# tuple - неизменяемый, итерируемый тип данных, который хранит в себе любой тип данных.

# list1 = [1,2,3]
# tuple1 = (1, 2, 3, 2, 4, 2)

# print(tuple1.index(3))  # 2

# list1 = [1,2,3]
# list2 = [1,2,3]
# list1 is list2

'--------------------------------------------------------'
# tuple1 = (1,2,3)
# tuple2 = (1,2,3)

# tuple1 is tuple2

# tuple1 = (12,)
# print(type(tuple1))

# print(dir(tuple))

# tuple1 = (1,2,3)
# tuple2 = (1,2,3)

# print(id(tuple1))
# print(id(tuple2))

# '--------------------------'

# list1 = [1,2,3]
# list2 = [1,2,3]

# print(id(list1))
# print(id(list2))

# list1 = ['hi', 'katana', 'hi', 'hello']
# set1 = set(list1)
# list2 = list(set1)
# print(list2)


'=========================================================================================================================='
# sudo apt install python3.12 - команда обновления питона

# relsy1 = ['grusha', 'apple', 'ananas', 'banan']
# meshok = {frukty for frukty in relsy1}
# print(meshok)
# {'grusha', 'apple', 'ananas', 'banan'}


# У вас есть list5 = [12, 4, 3, 4, 56, 8, 9, 0, 0, 23, 34]
# вам нужно удалить все похожие элементы и оставить уникальные, в конце должен полкчится list
# list5 = [12, 4, 3, 4, 56, 8, 9, 0, 0, 23, 34]
# set1 = set(list5)
# list5 = list(set1)
# print(list5)


# count = 0
# while count < 10:
#     count += 1
#     print(count)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
