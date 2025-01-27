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
# print(x ** 0.5) #нашли кв koren cherez formulu

# from math import sqrt
# #iz faila importiruy eto

# print(sqrt (x)) # nashli kv koren cherez funkciyu sqrt

#pow
# 1) vozvodit v stepen
# 2) nahodit ostatok
#print(pow(5, 3, 2, 4)) # (5 ** 3) % 2 = 1

str1 = 'metalabs '
num1 = 2

#print(str1 + num1) # error
#print(str1 * num1) # viydet 100 raz metalabs

str1 = 'hello '
str2 = 'world'
# print(str1 + str2) #hello world

#konkatenaciya - process slojeniya strok

# name = input('Vvedite imya: ')
# age = int(input('Vvedite svoy vozrast: '))
# print(f'Menya zovut {name} mne {age} let')

# # print(type(name))
# # print(type(age))


#print(int('124')) # '124' -> 124

# print('Privet\nmir') #\n perenosit stroku vniz
# print('Privet\tmir') #\t dobavlyaet tabulyaciyu(neskolko probelov)
# print('\tPrivet\n\tmir')

#ekranirovanie - ispolzovanie komand vnutri stroki


#print(len('hello world')) #11, koll-vo simvolov v stroke

#index - numeraciya posledovatelnosti, nachbinaetsya s 0
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

#srezy [start:end:step] - eto chast stroki # старт конец и шаг важно запоимнить!