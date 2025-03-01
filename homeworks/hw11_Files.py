# # 1
# file = open('hmw.txt', 'r')
# print(file.read())
# file.close

# # 2
# log = str(input('Введите логин: '))
# pas = str(input('Введите пароль: '))

# file = open('users.txt', 'w')
# file.writelines([log, pas])
# file.close()

# # 3
# with open('hmw.txt', 'r') as file:
#     letter = file.read()
#     if 'w' in letter:
#         print('Да, в тексте есть w')
#     else:
#         print('Нет, в тексте нет w')

# # 4
# o_words = []

# with open('python.txt', 'r') as file:
#     let = file.read()
#     words = let.split()
#     for word in words:
#         if 'o' in word:
#             o_words.append(word)
# print(o_words)

# # 5
# with open('hmw.txt', 'r') as file:
#     rev = file.read()
#     for i in rev[::-1]:
#         print(i, end='')

# # 6
# res = []
# with open('sixth_task.txt', 'r') as file:
#     num = file.read()
#     for i in num:
#         if i.isdigit():
#             res.append(int(i))
#             print(sum(res))

