'===================Built-ins=================='
# # 1
# names = ['Nikita', 'Katana', 'Toma']
# ages = [25, 30, 35]
# zip1 = zip(names,ages)
# print(list(zip1))

# # 2
# text = 'python'
# text1 = enumerate(text,1)
# print(list(text1))

# # 3
# numbers = ['10', '20', '30', '40']
# mapped = map(int, numbers)
# print(list(mapped))

# # 4
# words = ['apple', 'banana', 'cherry', 'dog', 'elephant']
# filtered = filter(lambda x: x[0] == 'd',words)
# print(list(filtered))

# letter = 'd'
# filtered = filter(lambda word: letter in word, words)
# print(list(filtered))

# 5
# numbers = [1, -2, 3, -4, 5, -6]

# filtered = filter(lambda num: num > 0, numbers)
# mapped = map(lambda x: x ** 2, filtered)
# print(list(mapped))

# 6
# students = ['Alice', 'Bob', 'Charlie', 'David']
# scores = [85, 92, 78, 90]
# # zip2 = zip(students, scores)
# scored = filter(lambda y: y > 80, scores)
# zip_ = zip(students, scored)
# enum = enumerate(zip_, 1)
# mapped = map(tuple, enum)
# print(list(mapped))


