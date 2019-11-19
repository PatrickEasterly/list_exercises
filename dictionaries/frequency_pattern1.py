# list1 = [1,2,3,4]
# # list2 = [1,2,3,3]
# list2 = [1,4,3,2, 2]

# list1 = [1,2,3,4]
# list2 = [1,2,3,5]



dictionario = {}

def dictionary_maker(list):
    new_dict = {}
    dictionario = {}
    for letter in list:

        new_dict[letter] = list.count(letter)
    return new_dict

def compare(dict1, dict2):
    final = True
    for item in dict1:
        if dict2[item] not in dict1:
            final = False
        if dict2[item] == dict1[item]:
            final = True
    return final
        
    
# a = dictionary_maker(list1)
# b = dictionary_maker(list2)
a = list('pie')
b = list('eip')

print(a)
print(b)
print(compare(a, b))