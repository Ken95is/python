# 1
# def func1(func):
#     def wrapper(*args, **kwargs):
#         print('Выполнение функции...')
#         func()
#     return wrapper
# @func1
# def func2():
#     print("*")

# func2()
# # # func1(func2)() # если без @func1

# 2
# def mul(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs) * 2
#     return wrapper

# @mul
# def func():
#     res = 5 + 1
#     return res
# func()
# print(func())

# 3
# def voskl(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs) + '!'
#     return wrapper

# @voskl
# def slovo():
#     # slovo = 'hi' # 
#     slovo = str(input())
#     return slovo

# print(slovo())

# 4
# def vizov(func):
#     def wrapper(*args, **kwargs):

#         if func:
#             return func(*args, **kwargs)
#         else:
#             return 'Функция больше недоступна'

# @vizov       
# def func2():
#     return ('hi')

# print(func2)()()()   

'----------------'

def limit_calls(max_calls):   # я не смог сам решить поэтому посмотрел решение, но то что делал не удалял пока
    def decorator(func):
        # Счетчик вызовов
        calls = 0
        
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                return f'Функция больше не доступна. Лимит {max_calls} вызовов достигнут.'
        
        return wrapper
    return decorator

@limit_calls(3)
def func():
    return 'Функция выполнена'

print(func())
print(func())
print(func())
print(func())

# 5
# a = int(input())
# b = int(input())

# def argum(func):
#     def wrapper(*args, **kwargs):
#         print(f"Arguments:{a}, {b} ", args, kwargs)
#         return func(*args, **kwargs)
#     return wrapper

# @argum
# def func4():
#     return a + b
# print(func4())