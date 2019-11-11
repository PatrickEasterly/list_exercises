#define a list
# grocery_list = ['bacon', 'axe body spray', 'monster energy']

##add to the end
# grocery_list.append('beer')

##add to the beginning
# grocery_list.insert(0, 'blankets')

##slice from index 0 up to, but not including 3
# print(f'groceries 1 - 3: {grocery_list[0: 3]}')

# list_len = len(grocery_list)
# print(list_len)

# for loops
# for item in grocery_list:
#     print(f'You need to buy: {item}')

#while loop
# index = 0
# while index < len(grocery_list):
#     print('buy buy buy ' + grocery_list[index] + '\n')
#     index += 1

# remove from the end of a list
# grocery_list.pop()

# print(grocery_list)

#join two lists
# snacks = ['chips', 'crackers']
# grocery_list.extend(snacks)
# print(grocery_list)
#or
# wooks = ['ryan', 'austin']
# grocery_list += wooks
# print(grocery_list)
# grocery_list.pop()
# grocery_list.pop()
# print(grocery_list)

#split a string
# my_word = 'word'
# my_word = list(my_word)
# print(my_word)

# join items
# my_word = ''.join(my_word)
# print(my_word)

#how do I create a list of lists
pat_list = ['pat1', 'pat', 'pat']
dave_list = ['dave', 'dave']
all_list = [pat_list, dave_list]
print(all_list)

print(all_list[0][0])

pat_list.remove('pat')
print(pat_list)









# import from another file

from function_test import abc
# print(abc(1, 3))
