'===========================Модули и пакеты============================='
# любой файл с расширением '.py' - это модуль

# пакеты - набор модулей (обязательно должен быть файл __init__.py)

'==========================Работа с файлами==========================='
# open - это функция, которая открывает файл в определенном режиме
'режимы'

# r - read(только для чтения)
# w - write(только для записи, каждый раз когда вы открываете файл в режиме записи, то что было внутри очищается)
# a - append(только для дозаписи, добавляет в конец)
# x - создает файл, но если такой есть то выйдет ошибка
# b - binary (в бинарном виде)   # нужно отдельно прочитать

'---------------------Read-----------------------'
# file = open('test.txt', 'r')
# print(file.read())
# file.seek(0)   # перенос каретки на 0 символ
# print(file.read())
# # print(file.writable())
# print(file.readable())
# print(file.read(3))
# print(file.read(3))

# file.seek(0)
# print(file.readlines())  # читает каждую строку и возвращает список со строками
# file.seek(0)
# print(file.readline())

# print(file.tell())  # показывает где курсор

# file.close()
# print(file.closed)

# print(file.readline(5))
# print(file.readline(5))

'-------------------------------------------'
# import random
# number = random.randint(1,20)
# print(number)
'-------------------------------------------'




'--------------------------Write-----------------------'
# file = open('test.txt', 'w')
# если файла нет - создаст его

# file.write('HELLOWORLD\nPython')

# print(file.writable())
# file.read()
# print(file.readable())

# file.writelines(['hello\n', 'world\n', 'metalabs'])

# file.close()

# write - очищает файл и записывает строки, принимает строку
# writelines - очищает файл и записывает строки, принимает лист со строками

'----------------------append------------------------'
# file = open('test.txt', 'a')

# # file.write('\nNew line')
# file.writelines(['sdasd', 'adfgsh'])
# file.close()

# write - дозаписывает строки в конец, принимает строку
# writelines - дозазаписывает строки в конец, принимает лист со строками

'---------------------Контекстный менеджер------------------------'

# with open('test.txt', 'r') as file:
#     print(file.read())
#     file.read()
# print(file.closed)
# print('hi')

with open('test.txt', 'w+') as file:
# r+ - read append
    file.write('hi')
    file.seek(0)
    print(file.read())
