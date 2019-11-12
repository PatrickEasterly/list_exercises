# sum given numbers
# a = 4
# b = 3
# print(a + b)

# return the largest number 

# my_list = [1, 2, 3, 5, 2, 9, 1]
# print(max(my_list))

# return the smalles number

# my_list = [1, 2, 3, 5, 2, 9, 1]
# print(min(my_list))

# sort the numbers in a list
# my_list = [5, 6, 2, 1, 9]
# my_list.sort()
# print(my_list)

# given a ist of numbers, print each number in the list that is even

# my_list = [5, 6, 2, 1, 9, 8]

# for x in my_list:
#     if x % 2 == 0:
#         print(x)

# given a list of numbers, print the positive numbers

# my_list = [5, 6, 2, 1, 9, -15, -23]
# for x in my_list:
#     if x > 0:
#         print(x)
#     else: 
#         print('too small')

# given a list of numbers, put the positive numbers in a new list

# my_list = [5, 6, 2, 1, 9, -15, -23]
# new_list = []
# for x in my_list:
#     if x > 0:
#         new_list.append(x)
# print(new_list)

# given a list of numbers and a factor, multiply each item by factor. 
# put that in a new list

# my_list = [5, 6, 2, 1, 9, -15, -23]
# factor = 4
# new_list = []
# for x in my_list:
#     # x = x * factor
#     new_list.append(x * factor)
# print(new_list)

# multiply vectors
# list1 = [2, 4, 6]
# list2 = [5, 7, 9]
# list3 = []
# for i in range(len(list1)):
#     list3.append(list1[i] * list2[i])
# print(list3)

# matrix addition

# [[1, 3],     [[5, 2],
#  [2, 4]]  +   [1, 0]]

# matrix1 = [[1, 3, 1], [2, 4, 1], [1, 1, 1]]
# matrix2 = [[5, 2, 1], [1, 0, 1], [1, 1, 1]]
# matrix3 = []
# for i in range(len(matrix1)):
#     matrix3.append([])
#     for j in range(len(matrix1[0])):
#         matrix3[i].append(matrix1[i][j] + matrix2[i][j])

# print(matrix3)

# given a list of numbers or strings, create a new list with the same elements - diplicate values

# the_list = ['string', 1, 5, 5, 'string', 3, 'word']

# newlist = []
# index = 0
# while index < len(the_list):
#     temp = the_list[index]
#     index += 1
#     if temp not in newlist:
#         newlist.append(temp)
# print(newlist)

