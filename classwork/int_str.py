'======================================================int/str==========================================================='

# int - это целочислительный тип данных
num = 17

# float - это вещественые числа (тип данных)
num2 = 0.5

# decimal - это вещественное число, но более точнее (тип данных)
num3 = 0.5000000000

#complex - не проходим

# str - это строковый тип данных
str1 = 'Привет'

str2 = """Hi"""
str3 = '''Hi'''

# print(str1)

'=========================================Операции над INT/STR====================================================='

num1 = 10
num2 = 3

res = num1 * num2
# print(res)

# print(num1 * num2)

res = num1 + num2 #13
res = num1 - num2 #7

res1 = num1 / num2 #вещественное деление

res2 = num1 // num2 #целое деление
# print(res1, res2)



x = 5
y = 3

result1 = x ** y #5 * 5 * 5 = 125
result2 = y ** x #3 * 3 * 3 * 3 * 3 = 243
# print(result1, result2)


x = 10
y = 3

# print(x % y) # 1
# print (10 % 5) #0


# x = 81
# print(x ** 0.5) #нашли кв корень через формулу

# from math import sqrt
# # из файла импортируй это

# print(sqrt (x)) # нашли кв корень через функцию sqrt

#pow
# 1) возводит в степень
# 2) находит остаток
#print(pow(5, 3, 2, 4)) # (5 ** 3) % 2 = 1

str1 = 'metalabs '
num1 = 2

#print(str1 + num1) # error
#print(str1 * num1) # выйдет 100 раз metalabs

str1 = 'hello '
str2 = 'world'
# print(str1 + str2) #hello world

# конкатенация - процесс сложения строк

# name = input('Vvedite imya: ')
# age = int(input('Vvedite svoy vozrast: '))
# print(f'Menya zovut {name} mne {age} let')

# # print(type(name))
# # print(type(age))


# print(int('124')) # '124' -> 124

# print('Привет\nмир') #\n переносит строку вниз
# print('Привет\tмир') #\t добавляет табуляцию(несколько пробелов)
# print('\tПривет\n\tмир')

# экранирование - использование комманд внутри строки


# print(len('hello world')) #11, кол-во символов в строке

#index - нумерация последовательности, начинается с 0
#'m e t a l a b s'
# 0 1 2 3 4 5 6 7
#       ...-3-2-1

str1 ='hello world'
# print(str1[4]) #o
# print(str1[10]) #d
str2 = 'adsfsdfsdfsdgasgsdgssfs'
# print(str2[-1])

print(str1[0:5]) #hello
print(str1[::2]) #hlowrd - перепрыгнул
print(str1[::-1]) #dlrow olleh 
#srezy [start:end:step] - это часть строки # старт конец и шаг важно запомнить!
