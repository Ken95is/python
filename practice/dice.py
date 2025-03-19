import random


# dice = input('Roll the dice?: [y/n] ').lower()

# if dice == 'y':
#     roll1 = random.randint(1, 6)
#     roll2 = random.randint(1, 6)
#     print(roll1, roll2)
# elif dice == 'n':
#     print('Thank you')
# else:
#     print('Invalid choice')


# while True:
#     dices = input('Roll the dice?: [y/n] \n').lower()

#     if dices == 'y':
#         roll1 = random.randint(1, 6)
#         roll2 = random.randint(1, 6)
#         print(f'You rolled: {roll1} and {roll2}')
#     elif dices == 'n':
#         print('Thank you')
#         break
#     else:
#         print('Invalid choice')

'---------------------------------------------------------------------------------------------------'

list1 = ['rock', 'paper', 'scissor']

rps = input('r/p/s:  ').lower()
if rps not in list1:
    print('Error')
else:
    choice = random.randint(0,2)
    comp_choice = list1[choice]
    print(f'Computer choice: {comp_choice}')

    if (rps == 'rock' and comp_choice == 'scissor') or (rps == 'paper' and comp_choice == 'rock') or rps == ('scissor' and comp_choice == 'paper'):
        print('You win')
    elif rps == 'rock' and comp_choice == 'rock' or rps == 'paper' and comp_choice == 'paper' or rps == 'scissor' and comp_choice == 'scissor':
        print('Draw')
    else:
        print('You lose')


# list1 = ['Adilet', 'Ali', 'Emir', 'Beknur', 'Zhanuzak', 'Umar', 'Tima', 'Aiperi', 'Laura', 'Kanykei', 'Iskender']

# for i in [1,2,3]:
#     index = random.randint(0,10)
#     print(list1[index])


# from math import log

# def num_length(num):
#     l = log(num, 10)
#     return round(l)

# print(num_length(4221))

# num = 4221
# num2 = len(str(num))
# print(num2)

# num = 4221
# while num >= 10:
#     num2 = num // 10
#     print(num2)
#     num = num2

# num = 4221
# length = 0

# while num > 0:
#     num = num // 10
#     length += 1
#     print(length)

# num = 4221
# length = 0

# # Count the number of digits by dividing by 10
# while num > 0:
#     num //= 10  # Integer division to remove the last digit
#     length += 1  # Increment the length

# print(f"The length of the number is: {length}")