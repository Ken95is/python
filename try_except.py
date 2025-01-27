'==============================Exceptions=========================================='
# Исключения - обьекты, которые прерывают работу кода, если они не обработаны

# Ошибки - обьекты, которые прерывают работу кода, но их нельзя обработать, не считая исключения
IndexError
# исключение, которое выходит, когда мы обращаемся по несуществуещему индексу
'''
list_1 = [23, 15, 4, 2]
list_1[1000]
'IndexError: list index out of range'
'''

'''
list2 = [12, 23, 2, 1]
list2.pop(1000)
IndexError: pop index out of range
'''

'''
list3 =[]
list3.pop()
IndexError: pop from empty list
'''

KeyError 
# исключение, которое выходит, когда обращаемся по несуществуещему ключу
'''
dict1 = {'a':1}
dict1['b']
KeyError:'b'
'''

ValueError
# когда мы передаем в фунцию не коректный для нее тип данных
# когда мы распаковываем итерируемый обьект на несколько переменных и кол-во переменных не совпадает с кол-вом элементов
# в итерируемом обьекте
'''
int('10d')
ValueError: invalid literal for int() with base 10: '10d'
'''

# a = 1
# b = 3 # <=одинаково=> a, b, c = 1, 3, 5
# c = 5
'''
a, b, c = [1, 3, 5, 6]
ValueError: too many values to unpack (expected 3)
'''

TypeError
# выходит когда мы пытаемся использовать метод не свойственный какому-то типу данных
# когда мы пытаемся передать функции больше или меньше аргументов, чем принимает функция
'''
for i in 12345678:
    ...
TypeError: 'int' object is not iterable
'''

'''
5 + '5'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

'''
'5' + 5
TypeError: can only concatenate str (not "int") to str
'''

'''
{[1,2,3]:'hello'}
TypeError: unhashable type: 'list'
'''

'''
input('enter', 2)
TypeError: input expected at most 1 argument, got 2
'''
'''
list1 = []
list1.append()
TypeError: append() takes exactly one argument (0 given)

[].append()
'''

ZeroDivisionError
# выходит при делении на 0
'''
45 / 0
ZeroDivisionError: division by zero
'''
'''
45 // 0
ZeroDivisionError: integer division or modulo by zero
'''
'''
3 % 0
ZeroDivisionError: integer division or modulo by zero
'''

AttributeError
# выходит, когда мы обращаемся к несуществуещему аттрибуту или методу обьекта (типа данных)

'''
[].replace('','a')
AttributeError: 'list' object has no attribute 'replace'
'''
