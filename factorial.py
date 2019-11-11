# counter = 1
# sum = 0
# fact = 0
# while sum < 1000000:
#     fact = counter
#     sum = fact
#     print(fact, counter, sum)
#     while fact > 1:
#         fact -= 1
#         sum *= fact
#     counter += 1
# print('test')
# print(counter)

# factor = int(input('Enter a number to get its factorial '))

  ## recusive ##
# def factorial(num):
#     if num == 1:
#         return num
#     else: 
#         return num * (factorial(num - 1))
# factor = 1
# while factorial(factor) < 1000000:
#     factorial(factor)
#     factor += 1
# print(factor)

  ## TA's solution
# count = 1
# product = 1
# while product < 1000000:
#     count = count + 1
#     product = product * count

# print(count, '\n')
