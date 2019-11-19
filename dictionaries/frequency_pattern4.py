a = 'pie'
b = 'eip'

def anagram(string):
    string = list(string)
    new_dict = {}
    for letter in string:
        new_dict[letter] = string.count(letter)
    return new_dict

print(anagram(a))

def compare(dict1, dict2):
    dict1 = anagram(dict1)
    dict2 = anagram(dict2)
    count = 0
    if len(a) != len(b):
        print('Is false')
        return
    
    # is_anagram = True
    for item in dict1:
        for letter in dict2:
            if item == letter:
                count += 1

    if count == len(dict1):
        print("True")

    # return is_anagram

print(compare(a, b))
