# print 1-10
# a = 0
# while a < 10:
#     a += 1
#     print(a)

# print from chosen start to chosen end
# set_start = int(input('Start from: '))
# set_end = int(input('End on: '))
# s = set_start
# e = set_end
# while s <= e:
#     print(s)
#     s += 1

# print each odd number 1-10
# p = 1
# while p < 10:
#     print(p)
#     p += 2
#alt
# p = 0
# while p < 10:
#     if p % 2 != 0:
#         print(p)
#     p += 1

# do you want a coin
# count = 0
# game = True
# while game == True:
#     want = input('Do you want a coin? ')
#     if want == 'yes': 
#         count += 1
#         print(f'You have {count} coins. ')
#     if want == 'no':
#         game = False
#         print('Bye')

# print 5 *s by 5 *s

# count = 0
# print('\n')
# while count < 5:
#     count += 1
#     print('*****')

# print box with given dimensions
# width = int(input('Width? '))
# height = int(input('Height? '))
# top = '*' * width
# bottom = '*' * width
# ends = '*' + ((height - 2) * ' ') + '*'
# print(top)
# count = 0
# while count < (height - 2):
#     count += 1
#     print(ends)
# print(bottom)

# print a triangle
# print('   *   \n  ***  \n ***** \n*******')

#print triangle with given height

# height = int(input('Triangle height: '))
# row = (height * 2) - 1
# spaces = int((row - 1) / 2)

# spaces_print = int((row - 1) / 2) * ' '
#     # 4
#     3 1 3
#     2 3 2
#     1 5 1
#     0 7 0
#     # 5
#     4 1 4
#     3 3 3
#     2 5 2
#     1 7 1
#     0 9 0
# stars = 1
# star_print = '*'
# while stars < (height * 2):
#     print(spaces_print, star_print, spaces_print)
#     spaces -= 1
#     stars += 2
#     star_print = stars * '*'
#     spaces_print = (spaces) * ' '

# multiplication tables

# multiplier = 1
# tab = 1
# while tab < 11:
#     while multiplier < 11:
#         result = tab * multiplier
#         print(f'{tab} X {multiplier} = {result}')
#         multiplier += 1
#     multiplier = 1
#     tab += 1
text = input('Your text to be made into a magical banner: ')
len = len(text)
bread = (len + 4) * '*'
mid = f'* {text} *'
# print(bread,mid,bread)

second = f'''
{bread}
{mid}
{bread}'''
print(second)