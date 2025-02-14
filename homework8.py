# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
operation = input('Введите операцию: ')
dict1 = {'+': lambda num1,num2: num1 + num2,
        '-': lambda num1,num2: num1 - num2,
        '*': lambda num1,num2: num1 * num2,
        '/': lambda num1,num2: num1 / num2
        }

# if operation == '+':
#     print(dict1['+'](num1,num2))
# elif operation == '-':
#     print(dict1['-'](num1,num2))
# elif operation == '*':
#     print(dict1['*'](num1,num2))
# elif operation == '/':
#     print(dict1['/'](num1,num2))   # делал сам try-except не получилось

# if operation in dict1:
#     try:
#         num1 / num2
#         result = dict1[operation](num1,num2)
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')


    
    
if operation in dict1:   # подсмотрел в chatgpt
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        result = dict1[operation](num1, num2)
        print(f"Результат: {result}")
    except ZeroDivisionError:
            print("На ноль делить нельзя")


