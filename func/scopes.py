'======================Области видимости======================'
# LEGB - local enclosed global build-in

'======================Build-in========================'
# встроенное пространство имён (list, print, input, string, set, len)

'======================Global======================='
# пространство в файле, в котором мы пишем код
# globals() - это функция, которая показывает переменные и функции внутри глобального пространства(в файле)

'======================Local========================'
# локальное пространство - это пространство которое находится внутри функций
# var = ' global'

# def func():
#     var = 'local'
#     print(locals())

# print(var)
# func()
# global
# local

'===================Enclosed====================='
# замкнутое пространство - которое является локальным, у которого есть внутри локальное пространство

# var = 'global'

# def func():
#     var = 'enclosed'
#     print(var)

#     def inner_func():
#         var = 'local'
#         print(var)

#     inner_func()

# print(var)
# func()

'-------------------------------------------------------------'
# локальное пространство видит переменные из глобального пространства
# a = 'local'
# def func():
#     print(a)

# func()

'--------------------------------------------------------------'
# глобальное пространство не видит переменные из локального пространства
# def func():
#     a = 'local'

# print(a)
'--------------------------------------------------------------'


# count = 1

# def increase_count():
#     global count
#     print(count)
#     count += 1

# increase_count() # 1
# increase_count() # 2
# increase_count() # 3


def count(i):
    counter = 0

    def increase_counter():
        nonlocal counter
        print(counter)
        counter += 1

    for elem in range(i):
        increase_counter()

    
count(5)