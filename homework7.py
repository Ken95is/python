'===============Functions===================='
# 1
# def sum(x,y=7.89 / 100):
#     return x * y

# my_sum = sum(float(input('Введите сумму: ')))
# print(my_sum)

# 2

# def extr_nums(text):
#     numbers = ''.join(char for char in text if char.isdigit())
#     return int(numbers)
# str_ = input()
# print(extr_nums(str_))


# 3
# def year(x):
#     return x * 12 * 30

# def month(y):
#     return y * 30


# age = year(int(input('Введите кол-во лет: ')))
# age2 = month(int(input('Введите кол-во месяцев: ')))
# print('Кол-во дней: ',age + age2)

# 4

def dict1(**dict2):
    dict2 = {i:i ** 2 for i in range(1,11)}
    return dict2
print(dict1())


# 5

# def my_sum():
#     total = 0
#     for x in range(51):
#         print(total)
#         total += x
#     return total

# print(my_sum())