'===========================Comprehensions==============================='
# генератор, с помощью которого мы можем создать последовательность используя цикл for в одну строку

# элемент for переменная in последовательность
# элемент for переменная in последовательность if условие
# элемент1 if условие1 else элемент2 for переменная in последовательность
# элемент1 if условие1 else элемент2 for переменная in последовательность if фильтр

# list1 = ['hello' if num % 2 == 0 else 'world' for num in range(50) if ]

'3 вида '
list
set #все 3 изменяемые
dict


# comp = (i**2 for i in range(11))
# print(comp)
# print(list(comp))
# print(set(comp))

# comp = [i**2 for i in range(11)] #[] - скобки list,  {} = set
# print(comp)

# comp = [i for i in range(11) if i % 2 == 0]
# print(comp)

#list1 = [-12, 93, 0, 4, -1]
#list2 = ['-', '+', '+', '+', '-]

# list1 = [-12, 93, 0, 4, -1]
# list2 = ['+' if i >= 0 else '-' for i in list1]
# print(list2)


# list1 = [-12, 93, 0, 4, -1]
# list2 = []
# for i in list1:
#     if i >= 0:
#         list2.append('+')
#     else:
#         list2.append('-')
# print(list2)

# задачи
# [1,2,3,5,5]
# ['нечетный', 'четный', 'нечетный', 'нечетный', 'нечетный']

# {'a':1, 'b':2}
# {1: 'a', 2:'b}

#codewars
#stepik