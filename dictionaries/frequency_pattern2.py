# list1 = [1,2,3,4]
# list2 = [1,4,9,16]


# def make_dict(list):
#     new_dict = {}
#     for num in list:
#         new_dict[(num * num)] = list.count(num)
#     return new_dict
# def make_dict_square(list):
#     new_dict = {}
#     for num in list:
#         new_dict[num] = list.count(num)
#     return new_dict

# dict1 = make_dict(list1)
# dict2 = make_dict_square(list2)
# print(dict1)
# print(dict2)

# def compare(a, b):
#     does_contain = True
#     for item in a:
#         squared = item * item
#         # print(squared)
#         if squared not in b:
#             does_contain = False
#     return does_contain

# print(compare(dict1, dict2))

list1 = [1,2,3,4]
list2 = [1,4,9,16]

def dict_maker(list):
    new_dict = {}
    for item in list:
        new_dict[item] = item
    return new_dict

a = dict_maker(list1)
b = dict_maker(list2)

# print(a, b)

def compare(dict1, dict2):
    does_contain = True
    for item in dict1:
        if (item * item) not in dict2:
            does_contain = False
    return does_contain

print(compare(a, b))
