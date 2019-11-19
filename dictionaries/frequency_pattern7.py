

def split(word):
    return list(word)

def dictmaker(list):
    new_dict = {}
    for letter in list:
        new_dict[letter] = list.count(letter)
    return new_dict

def highest(dict):
    highest = ''
    for item in dict:
        for item2 in dict:
            if dict[item] >= dict[item2]:
                highest = item
    return highest

a = split('abcc')
b = (dictmaker(a))
print(highest(b))
