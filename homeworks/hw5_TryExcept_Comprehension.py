'Try-Except'
# '1'
# try:
#     raise ValueError
# except(ValueError):
#     print('Вышла ошибка: ValueError')  # не совсем понял задание


# '2'
# try:
#     int1 = int(input())
#     raise NameError
# except (NameError, ValueError):
#     print(int1, 'Такой переменной не существует!') # не думаю что правильно сделал

# '3'

# int1 = int(input())
# int2 = int(input())
# try:
#     int3 = int1 / int2
#     print(int3)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')

# '4'


# # try:   # не получилось таким способом
# #     int1 = int(input()) 
# #     int2 = int(input())
# #     if int1 % 1 == 0 and int2 % 1 == 0:
# #         print(int1 + int2)
# #     elif int1 % 1 != 0 and int2 % 1 != 0:
# #         int3 = int1 // 1
# #         int4 = int2 // 1
# #         print(int3 + int4)
# # except ValueError:
# #         print('Введите число!')


# try:
#     str1 = int(input('Введите 1 число '))
#     str2 = int(input('Введите 2 число '))
#     print(f'Сумма чисел:  {str1 + str2}')
# except ValueError:
#     print('Введите число ')

# '5'

# dict1 = {'1': 'a', '2': 'b'}
# try:
#     print(dict1[input('Введите ключ: ')])
# except KeyError:
#     print('Нет такого ключа!')

# '6'

# try:
#     str1 = 'qwerty '
#     print(str1[0:6])
#     print(str1[7])
# except IndexError:
#     print('Нет такого элемента')  # не уверен что правильно сделал, вроде работает

# '7'

# age = int(input('Возраст: '))
# try:
#     if age < 18:
#         print('доступ запрещен')
#         raise ValueError
# except:
#     v = 'Введен некоректный возраст'  # вроде работает, можно наверно сократить
#     print(v)
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

# '8'

# int1 = int(input())   # не удалось полностью, ValueError не работает
# int2 = int(input())
# try:
#     int3 = int1 // int2
#     print(int3)
#     raise ValueError
# except (ValueError, ZeroDivisionError):
#     print('Произошла ошибка!')

# '9'

# sum = int(input())
# try:
#     if sum < 0:
#         raise ValueError('Сумма не может быть отрицательной')
# except ValueError as e:
#     print(e)
# else:
#     print(sum)


# '10'
# try:
#     int1 = '5' + 5
#     print(int1)
# except TypeError:
#     print('Unsupported option')    # 2 способа, не уверен правильно ли сделал хоть один


# int1 = input()
# int2 = int(input())
# try:
#     int3 = int1 + int2
#     print(int3)
# except TypeError:
#     print('Unsupported option')

'Comprehensions'

#1
# list1 = [i ** 2 for i in range(11)]
# print(list1)

#2
# list2 = [i for i in range(21) if i % 2 == 0]
# print(list2)

# 3
dict2 = {i: i ** 2 for i in range(1, 6)}
print(dict2)

# 4
# words = ["python", "java", "swift", "golang", 'javascript']
# comp = [i for i in words if len(i) > 5]
# print(comp)

# # 5
# words = ["apple", "banana", "cherry"]
# comp = [i.upper() for i in words]
# print(comp)







'-------------------------------------------------------------------------------------------'
# # try:
# #     passw = input('password: ')
# #     if passw == '123456':
# #         print('you are in system') # для себя эту сделал
# #     elif passw != '123456':
# #         raise Exception('not right password')
# # except Exception as p:
# #     print(p)