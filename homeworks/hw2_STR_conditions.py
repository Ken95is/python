#str методы
#N1
# str1 = input('Исходная строка: ')
# print('Исходная строка: ', str1)
# print('Строка в верхнем регисьре: ',str1.upper())

#N2
# str2 = input("Напишите строку: ")
# print(str2.replace(' ', '-'))

#N3

# str3 = input('Напишите строку: ') #пробел в строке  выдает false
# print(str3.isalpha())

#N4

# str4 = input('Напишите строку: ')
# print(dir(str4))


#5
# str5 = input('Введите предложение: ')[:: -1]
# print(str5[0], str5[-1], str5)   #1 способ, только почему то сперва убирает последнюю букву потом первую

# print(str5[0]) # 2 способ
# print(str5[-1])
# print(str5)

# не знаю как срезать любое слово

#=======================================условные операторы===========================================================

#1
# x = int(input('Число: '))
# if x % 2 != 0:
#     print(f'Число {x} не является четным')
# else:
#     print(f'Число {x} является четным')

#2

# x = int(input('Число: '))
# x % 2 == 0 and x % 3 != 0 and x ** 2 > 1000 #недопонял задание. вроде бы как в задании сделал
# x ** 2 > 1000 and x % 3 != 0 and x % 2

#3

# a = int(input('a: '))
# b = int(input('b: '))
# if a % 2 == 0 and b % 2 == 0:
#     print("Эти числа положительные")

#4

# x = int(input('Возраст: '))
# if x >= 18 and x <= 120:
#     print('Совершенолетний')
# elif x >= 0 and x < 18:
#     print('Несовершенолетний')
# else:
#     print('Недопустимый возраст')

#5
# x = 13
# y = x ** 2
# if y < 172:
#     print(y ** 2)




'---------------------------------------------------------------'
# x = int(input('Год: '))
# y = int(input('mesyac: '))
# z = int(input('den: '))
# print(f'Год: {x}', f'mesyac: {y}',  f'den: {z}' )
