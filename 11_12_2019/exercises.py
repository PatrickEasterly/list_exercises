# https://dc-learning-portal.netlify.com/lessons/python/functions/#training-exercises

    # small

# madlib function

# def madlib(name, subject):
#     return f'{name} is the best student of {subject} in the world. '
# print(madlib('pat', 'coding'))

# C to F
# def c_to_f(temp):
#     return ((temp * (9/5)) + 32)
# print(c_to_f(0))

# F to C  

# def f_to_c(temp):
#     return ((temp -32) * (5/9))
# print(f_to_c(32))

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#          return False
# print(is_even(4))

# # is odd using is_even
# def is_odd(num):
#     if is_even(num) is not True:
#         return True
#     else:
#         return False
# print(is_odd(4))

# def only_evens(list):
#     new_list = []
#     for item in list:
#         if is_even(item) == True:
#             new_list.append(item)
#     return new_list
# print(only_evens([11, 20, 42, 97, 23, 10]))

# def only_odds(list):
#     new_list = []
#     for item in list:
#         if is_even(item) != True:
#             new_list.append(item)
#     return new_list
# print(only_odds([11, 20, 42, 97, 23, 10]))

    #medium

# find the smallest number 

# def smallest(list):
#     return min(list)
# print(smallest([2, 5, 6, 1]))

# find the largest number

# def largest(list):
#     return max(list)
# print(largest([2, 5, 6, 1]))

# find shortest string

# def shortest(list):
#     temp = [list[0]]
#     for item in list:
#         if len(item) < len(temp[0]):
#             temp[0] = item
#     print(temp)

# shortest(['aaa', 'bb', 'cccc'])

#find longest string
# def longest(list):
#     temp = ''
#     for item in list:
#         if len(item) > len(temp):
#             temp = item
#     return temp
# print(longest(['aaaaaaa', 'bb', 'ccccccccc', 'ddd']))

    # large

#tic-tac-toe

# board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# def move(board, location, player):
#     h = location[0]
#     w = location[1]

#     # invalid location
#     if h > 2 or w > 2:
#         print('Invalid location. Please choose a square between (0, 0) and (2, 2)')
#         return

#     # board too large
#     if len(board) != 3 or len(board[0]) != 3 or len(board[1]) != 3 or len(board[2]) != 3:
#         print('This board is too big. ')
#         return

#     # space already taken
#     if board[h][w] != ' ':
#         print('This space is already taken. ')
#         return
#     if board[h][w] == ' ':
#         board[h][w] = player


#     # print board
#     print(f'''
#     {board[0]}
#     {board[1]}
#     {board[2]}
#     ''')

# # [' ', 'x', ' '] board[0, 1]
# # [' ', 'x', ' '] board[1, 1]
# # [' ', 'x', ' '] board[2, 1]

# def checker(board):
#     winner = ''
#     for row in board:
#         if row[0] == row[1] == row[2]:
#             winner = row[0]
#         for space in row:

#     print(f'{winner} is the winner!')
# checker([['x', ' ', ' '], ['x', 'x', ' '], ['x', ' ', ' ']])

# change maker, with tuple output

# def change_maker(charge, given):
#     change = given - charge
#     ones = 0
#     fives = 0
#     tens = 0
#     twentys = 0
#     fiftys = 0
#     hundreds = 0
#     quarters = 0
#     dimes = 0
#     nickles = 0
#     pennies = 0
#     while change != 0:
#         if change > 100:
#             hundreds += 1
#             change -= 100
#         if change < 100 and change >= 50:
#             fiftys += 1
#             change -= 50
#         if change < 50 and change >= 20:
#             twentys += 1
#             change -= 20
#         if change < 20 and change >= 10:
#             tens += 1
#             change -= 10
#         if change < 10 and change >= 5:
#             fives += 1
#             change -= 5
#         if change < 5 and change >= 1:
#             ones += 1
#             change -= 1

#         if change < 1 and change >= 0.25:
#             quarters += 1
#             change -= 0.25
#             change = round(change, 2) 
#         if change < 0.25 and change >= 0.10:
#             dimes += 1
#             change -= 0.1
#             change = round(change, 2)     
#         if change < 0.10 and change >= 0.05:
#             nickles += 1
#             change -= 0.05
#             change = round(change, 2) 
#         if change < 0.05 and change >= 0.01:
#             pennies += 1
#             change -= 0.01
#             change = round(change, 2)        
#     # print(f'Change: {change}')
#     # print(f'Ones: {ones}')
#     # print(f'Fives: {fives}')
#     # print(f'Tens: {tens}')
#     # print(f'Twentys: {twentys}')
#     # print(f'Fiftys: {fiftys}')
#     # print(f'Hundreds: {hundreds}')
#     # print(f'Quarters: {quarters}')
#     # print(f'Dimes: {dimes}')
#     # print(f'Nickles: {nickles}')
#     # print(f'Pennies: {pennies}')

#     turple = ((ones, fives, tens, twentys, fiftys, hundreds),(pennies, nickles, dimes, quarters))
#     print(turple)

# change_maker(1.01, 5)

# change maker, with QuikTrip output


# def change_maker(charge, given):
#     change = given - charge
#     # declare bills and coins, set them to zero
#     ones, fives, tens, twentys, fiftys, hundreds, quarters, dimes, nickles, pennies = (0,)*10
#     # down the line
#     while change != 0:
#         if change > 100:
#             hundreds += 1
#             change -= 100
#         if change < 100 and change >= 50:
#             fiftys += 1
#             change -= 50
#         if change < 50 and change >= 20:
#             twentys += 1
#             change -= 20
#         if change < 20 and change >= 10:
#             tens += 1
#             change -= 10
#         if change < 10 and change >= 5:
#             fives += 1
#             change -= 5
#         if change < 5 and change >= 1:
#             ones += 1
#             change -= 1

#         if change < 1 and change >= 0.25:
#             quarters += 1
#             change -= 0.25
#             change = round(change, 2) 
#         if change < 0.25 and change >= 0.10:
#             dimes += 1
#             change -= 0.1
#             change = round(change, 2)     
#         if change < 0.10 and change >= 0.05:
#             nickles += 1
#             change -= 0.05
#             change = round(change, 2) 
#         if change < 0.05 and change >= 0.01:
#             pennies += 1
#             change -= 0.01
#             change = round(change, 2)       
     
#     print(f'Change: {change}')
#     print(f'Ones: {ones}')
#     print(f'Fives: {fives}')
#     print(f'Tens: {tens}')
#     print(f'Twentys: {twentys}')
#     print(f'Fiftys: {fiftys}')
#     print(f'Hundreds: {hundreds}')
#     print(f'Quarters: {quarters}')
#     print(f'Dimes: {dimes}')
#     print(f'Nickles: {nickles}')
#     print(f'Pennies: {pennies}')

#     # turple = ((ones, fives, tens, twentys, fiftys, hundreds),(pennies, nickles, dimes, quarters))
#     # print(turple)

# cashier = float(input('Your total today is: $'))
# customer = float(input('Ok, here\'s $'))
# change_maker(cashier, customer)

# change value

# def value_of_change(change):
#     total = 0
#     total += change[0][0]
#     total += change[0][1] * 5
#     total += change[0][2] * 10
#     total += change[0][3] * 20
#     total += change[0][4] * 50
#     total += change[0][5] * 100
#     total += change[1][0] * 0.01
#     total += change[1][1] * 0.05
#     total += change[1][2] * 0.1
#     total += change[1][3] * 0.25

#     print(total)

# value_of_change(((3, 0, 1, 1, 0, 1), (4, 1, 0, 2)
# ))
