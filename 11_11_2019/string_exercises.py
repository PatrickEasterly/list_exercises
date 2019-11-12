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

def leetspeak(name):
    name = name.upper()
    name = name.replace("L", "1")
    name = name.replace("E", "3")
    name = name.replace("T", "7")
    name = name.replace("S", "5")
    name = name.replace("O", "0")
    name = name.replace("A", "4")
    name = name.replace("G", "6")
    return name

strang = input('What would you like to translate? ')
print(leetspeak(strang))