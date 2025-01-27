'=====================List(Списки)================'
# списки - это упорядоченный, индексируемый, итерируемый, изменяемый тип данных

# list1 = [12, 'hi', True, False, None, 20.5]
# print(list1[-1])

# list, set, dict

# str, int, boolean, NoneType, Tuple, float, decimal, frozenset

# str1 = 'hello'
# print(str1.replace('l', 'd')) # heddo
# print(str1)


# list1 = [31,62,13]
# print(list1.pop(1))
# poped_item = list1.pop(1) # удаляет элемент по индексу и возвращает удаленный элемент
# print(list1)
# list1 = [1,2,34,5,6,78,90,'hi', 232,'hello', True, 1,2,3,5,3,45,5]
# list1.remove('hello') # удаляет элемент по значение 
# print(list1)
# list1.append('hi') # добавляет элемент в конец
# print(list1)
# list2 = [1,'hi',True]
# list1.append(list2) 
# print(list1) # [31,62,13,[1,2,3]]
# list1.extend(list2)
# print(list1) # [31,62,13,1,2,3]


# print(dir(list))
# list1 = [4,5,6]
# list1.insert(1, 'hi')
# print(list1) # [4, 'hi', 5, 6]

# [1,2,3] -> [3,2,1]

# [134,2,64,2,0,1,56,3]
# [0,1,2,2,3,56,64,134]

# list1 = [3,745,2,54,99,0,1]
# list1.sort(reverse=True)
# print(list1)

'========================Циклы======================'
# циклы - это специальный блок кода который выполняет то что внутри несколько раз
# for  - работает до конца последовательности(итерируемого обьекта)
# while - работает пока условие True

'FOR'
# list1 = ['hi', 12, 4, True, False]
# str1 = 'hello'

# for item in list1: 
#     print(item) 


# meshok = ['kartoshka', 'luk', 'pomidor']

# for ruka in meshok:
#     if ruka == 'pomidor':
#         meshok.remove(ruka)
#     else:
#         print(ruka.upper())

# print(meshok)


'range(start, end, step) - функция которая создает числовой диапозон'

# range_ = list(range(45))
# print(range_)

# for любою_переменная in последовтельность:
#     код

# for i in 'hello':
#     print(i)

# for i in range(0, 51, 2):
#     print(i)

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)

'WHILE'
# count = 0
# while count < 10:
#     print(count)
#     count += 1 # count = count + 1

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9



'=========================================Break, contine============================================='

#break(ломать) - оператор который принудительно завершает работу цикла
#contine(продолжить) - оператор который пропускает итерацию если питон его встретит

#итерируемый обьект - последовательность по которой можно пройтись циклом
#итерация - круг в цикле, процесс прохождения

# for i in [1,2,3,4,5]:
#     if i == 3:
#         continue
#     print(i)

    #1
    #2
    #4
    #5

# for i in range(1,6):
#     print(i)
#     if i == 2:
#         continue
# 1
# 2
# 3
# 4
# 5

# for i in range(1,6):
#     print(i)
#     if i == 2:
#         continue
#     print('hello')

# 1
# hello
# 2
# 3
# hello
# 4
# hello
# 5

# for i in [1,2,3,4,5]:
#     if i == 4:
#         break
#     print(i)


# count = 0
# while count < 10:
#     if count == 3:
#         count += 1
#         continue
#     print(count)
#     count += 1 #count = count + 1

# 1
# 2
# 4
# 5
# 6
# 7
# 8
# 9

# count = 0
# while count < 10:
#     if count == 3:
#         break
# print(count)
# count += 1

# 0
# 1
# 2

# for i in [1,2,3,4,5]:
#     print(i)
#     if i == 10:
#         break
# else:
#     print('Цикл завершил работу')

# 1
# 2
# 3
# 4
# 5
# Цикл завершил работу


# count = 0
# while count < 10:
#     print(count)
#     if count == 3:
#         break
#     count += 1
# else:
#     print('hi')