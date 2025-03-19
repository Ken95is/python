# 1. Создайте файл data.json с произвольными данными.
# Напишите программу, которая загружает его содержимое в Python-объект и выводит на экран
import json

# with open('data.json') as file:
#     python_data = json.load(file)
#     print(python_data)
    

# 2) Создайте словарь с данными о пользователе (name, age, email).
# Запишите его в файл user.json

# user = {'name':'Sultan', 'age':21, 'email':'tlbkvs@gmail.com'}

# with open('user.json', 'w') as file:
#     json.dump(user, file)

# 3) Дана JSON-строка:
# product = '{"product": "Laptop", "price": 1200, "in_stock": true}'
# # Преобразуйте ее в Python-словарь и выведите значение ключа "price".

# with open('data.json') as file:
#     price = json.loads(product)
#     # price = price.get('price')
#     # print(price)
# print(price.get('price'))

# 4) Дан файл products.json с массивом товаров (id, name, price).
# Напишите функцию, которая принимает id товара и возвращает его данные.
# [
#   {"id": 1, "name": "Laptop", "price": 1200},
#   {"id": 2, "name": "Smartphone", "price": 800},
#   {"id": 3, "name": "Tablet", "price": 500}
# ]

# def get_info(x):
#     with open('products.json') as file:
#         products = json.load(file)
#         for i in products:
#             if x == i.get('id'):
#                 return i
            
# print(get_info(3))


# 5) Дан config.json с настройками программы:
# config = {
#   "theme": "light",
#   "language": "en",
#   "volume": 70
# }
# Напишите функцию, которая изменяет переданный параметр (например, theme → "dark") и сохраняет изменения.

# # def param():
# #     with open('config.json', 'w') as file:
# #         config["theme"] = "dark"
# #         return json.dump(config, file)
    
# # print(param())

# def param():
#     with open('config.json') as file:
#         tema = json.load(file)
#         if tema["theme"] == "light":
#             tema["theme"] = "dark"
#     with open('config.json', 'w') as file:
#         return json.dump(tema, file)
# print(param())

# 6) Дан students.json, содержащий список студентов с их баллами.
# Напишите функцию, которая фильтрует студентов с баллом выше 80 и сохраняет их в top_students.json.
# [
#   {"name": "Alice", "score": 85},
#   {"name": "Bob", "score": 78},
#   {"name": "Charlie", "score": 90},
#   {"name": "Dave", "score": 65}
# ]

# def top_stud():
#     with open('students.json') as file:
#         stud = json.load(file)
#         top_students = [i for i in stud if i.get('score', 0) > 80]
#         return top_students
#         # for i in stud:
#         #     if i.get('score') > 80:
#         #         return i
# print(top_stud())

# 7) Есть два файла: employees1.json и employees2.json, содержащие списки сотрудников.
# Напишите программу, которая объединяет их в один список и сохраняет в all_employees.json, исключая дубликаты

# employees1.json:
# [
#   {"id": 1, "name": "John Smith", "department": "HR"},
#   {"id": 2, "name": "Jane Doe", "department": "IT"}
# ]

# employees1.json:
# [
#   {"id": 2, "name": "Jane Doe", "department": "IT"},
#   {"id": 3, "name": "Emily Johnson", "department": "Marketing"}
# ]

# def all_emp():
#     with open('employees1.json') as file:
#         list1 = json.load(file)
#     with open('employees2.json') as file:
#         list2 = json.load(file)
#         list1.extend(list2)
#     with open('all_employees.json', 'w') as file:
#         return json.dump(list1, file)
# print(all_emp())

# 8) Создайте log.json, в который можно записывать события вида:
# {"timestamp": "2025-03-10 12:30:45", "event": "User logged in", "user_id": 123}
# Напишите функцию log_event(event, user_id), которая добавляет новую запись в этот файл.

# with open('log.json', 'a') as file:
#     log = {'timestamp:': str(input()),
#         'event:': str(input()),
#         'user_id:': int(input())}
#     json.dump(log, file)
#     file.write('\n')