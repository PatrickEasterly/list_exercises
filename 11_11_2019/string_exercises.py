#uppercase a string

# string = 'strang'
# string2 = string.upper()
# string2 = 'yeet'.upper()
# print(string2)

#capitalize a string

# string = 'strang gang'
# string2 = list(string)
# cap = string2[0]
# string2.remove(cap)
# string2.insert(0, cap.upper())
# final = ''.join(string2)
# print(final)

# reverse a string

# string = 'strang gang'
# string2 = list(string)
# print(string2)
# string3 = []
# index = -1
# for i in string2:
#     string3.append(string2[index])
#     index -= 1
# string3 = ''.join(string3)
# print(string3)

# can you do better?

# def reverse_it(a):
#     a = list(a)
#     b = []
#     c = ''
#     index = -1
#     for i in a:
#         b.append(a[index])
#         index -= 1
#     c = ''.join(b)
#     print(c)
# reverse_it('tweet')

#leetspeak 

# def leetspeak(name):
#     name = name.upper()
#     name = name.replace("L", "1")
#     name = name.replace("E", "3")
#     name = name.replace("T", "7")
#     name = name.replace("S", "5")
#     name = name.replace("O", "0")
#     name = name.replace("A", "4")
#     name = name.replace("G", "6")
#     return name

# strang = input('What would you like to translate? ')
# print(leetspeak(strang))

#long-long vowels

# def vowelize(string):
#     if 'oo' in string:
#         string = string.replace('oo', 'ooooo')
#     elif 'ee' in string:
#         string = string.replace('ee', 'eeeee')
#     else:
#         string = string
#     return string
# talk = input('talk: ')
# print(vowelize(talk))

# def vowelize(string):
#     no_vowels = []
#     for x in string:
#         if x not in 'aeiou':
#             no_vowels.append(x)
#     return ''.join(no_vowels)
# vowel_string = input('Let me take those vowels for you: ')
# print(vowelize(vowel_string))

# ceaser cipher

# string = 'ibh zhfg hayrnea jung lbh unir yrnearq'
# index = 0
# encrypted = ''
# alphabet = list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz ')
# while index < len(string):
#     temp = string[index]
#     index += 1
#     if temp == ' ':
#         encrypted += temp
#     else:
#         temp2 = alphabet[(alphabet.index(temp) + 13)]
#         encrypted += temp2
#     # print(temp2)

# print(encrypted)

# ibh zhfg hayrnea jung lbh unir yrnearq



# def cipher(string):
#     for char in string:
#         char = 


# print(ord('a'))
# # print(ord('pat'[0]))
# print( chr(int(ord('pat'[0])) + 5) )
