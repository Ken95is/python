'LISTS'
#1

# list1 = [1,2,3,4,5]
# list2 = [6]
# list1.append(list2) # 1 способ(append можно на extend)
# print(list1)

# list1 = [1,2,3,4,5]
# list1.insert(5,6) # 2 способ
# print(list1)


#2
# list1 = [1,2,3,4,5]
# print('Удаленный элемент ',list1.pop(2))
# # poped_item = list1.pop(2) #не уверен правильно ли
# print(('Обновленный список: '), list1)

# #3
# list2 = ['яблоко', 'банан', 'вишня'] #не совсем как в задании не удалось вывести удаленный элемент, надо спросить как правильно
# list2.remove('банан')
# list2.append('персик')
# print(list2)

#4
# list3 = [42, 13, 89, 7, 64, 22]
# list3.sort()
# print(list3)
# list3.sort(reverse=True)
# print(list3)

# #5
# list5 = [[1,2], [3,4], [5,6]]
# list6 = [7,8]
# list5.append(list6)
# print(list5)

'LOOPS'
#1

# for i in range(1,11):
#     print(i)

# count = 1
# while count < 11:
#     print(count)
#     count = count + 1

# 2
# for i in range(1,100):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# count = 1
# while count <= 100:
#     count +=1
#     if count % 3 == 0 and count % 5 == 0 :
#         print(count) 

# 3
# for i in range(1,100):
#     if i % 2 == 0 and i % 3 == 0 and i % 9 == 0:
#         print(i)

# count = 1
# while count <= 100:
#     count += 1
#     if count % 2 == 0 and count % 3 == 0 and count % 9 == 0 :
#         print(count)

# 4

# for i in range(1,300):
#     if i % 2 == 0:
#         print(i)
#     if i == 237:
#         break

#5

# "Ботнет IPStorm" = ['Windows-машины','увеличился до 13500 зараженных систем']
# my_string = "Ботнет IPStorm" #не понял задание, надо спросить
# my_string2 = sorted(my_string, key=int)
# print(my_string2)

# int1 = list(my_string)
# if int1.isdigit:
#     print(int1 * 2)