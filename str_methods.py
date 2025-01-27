#============================================Str методы===========================================================
str1 = 'Hello'
# res1 = str1.lower() #Hello -> hello
# print(res1)
# print(str1.upper()) #Hello -> HELLO

#print(dir(str1)) # команда для просмотра методов и атрибутов

str2 = 'HELLO'
# print(str2.swapcase()) #hELlO WoRlD
# print(str2.capitalize()) #Hello world
# print(str2.title()) #Hello World
# print(str2.replace('L', 'K', 2))

# print(str2.islower()) #false
# print(str2.isupper()) #true
str3 = 'hello'
# print(str3.isalpha()) #true
# print(str3.isdigit()) #false

str4 = 'asd123'
# print(str4.isalnum())

str5 = 'hello world2222'
# print(str5.count('l')) # 3

str5 = input('Введите предложение: ')[:: -1] #отзеркалит строку задом наперед вместе с нижней
print(str5) # отзеркалит строку задом наперед вместе с верхней
print(str5[0]) #уберет 1 букву
print(str5[-1]) #уберет последнюю букву

#===============================================BooleanType, NoneType==========================================
a = True #истина (да)
b = False #ложь (нет)
c = None #пустота


# print(bool(1)) #true
# print(bool(0)) #false
# print(bool(None)) #false
# print(bool('hello')) #true
# print(bool(' ')) #true
# print(bool('')) #false
# print(bool(-15)) #true


'===============================================Логические и условные операторы========================================='
#логические операторы - выраженияб которые возвращают True или False

'равенство'
10 == 5 #false
1 == 10 #true

'неравно'
10 != 5 #true
10 != 10 #false

'больше'
34 > 10 #true
20 > 20 #false
10 > 12 #false

'меньше'
23 < 10 #false
10 < 10 #false
10 < 24 #true

'больше или равно'
10 >= 5 #true
10 >= 10 #true
2 >= 5 #false

'меньше или равно'
23 <= 4 #false
23 <= 23 #true
23 <= 100 #true

# print(int('5') == 5)

'=====================================================And, Or, Not======================================================='
#and - и
#or - или
#not - не
"AND"
x = 5
y = 6

#true      true
x == 5 and y == 6 #true

#true   и  false   
x == 5 and y < 3 #true

#false   и        false
x >= 20 and y == -20 #false

'OR'
#false или true
x > 10 or y == 6 #true
#true     true
x == 5 or y == 6 #true
#false     false
x == 13 or y == 23 #false


'Not'
not True #false
not False #true

not 20 > 10 #false



x=12
y=4

#not x == 12 or y > 12 and x != 12 or y > 3 #true
#print(False or False  and False   or True)


#if условие1:
#    действие1:
#elif условие2:
#    действие2:
#elif условие3:
#else:
#    действие3

# pogoda = input('Какая погода? ')

# if pogoda == 'дождь':
#     print("взять зонтик")
# elif pogoda == 'снег':
#     print('взять шапку')
# elif pogoda == 'солнечно':
#     print('взять очки')
# else:
#     print('такой погоды нет')

# [start:end:step] !!!для себя запомнить


number = int(input("Число: "))

if number > 0:
    print(f"Число {number} положительное")
elif number < 0:
    print(f'Число {number} отрицательное')
else:
    print(f'Число {number} равно 0')