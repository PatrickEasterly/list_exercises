# https://dc-learning-portal.netlify.com/lessons/python/mapping/#small
##### Small

# #given the following dictionary, representing a maping from names to phone numbers

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# # write code to:
# # print Elizabeth's phone number

# el = phonebook_dict['Elizabeth']
# print(el)

# # add an entry to the dictionary: Kareem: 938-489-1234
# phonebook_dict['Kareem'] = '938-489-1234'
# print(phonebook_dict['Kareem'])

# # delete Alice's phone entry

# del phonebook_dict['Alice']
# print(phonebook_dict)

# # change Bob's phone number to 968-345-2345
# phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict['Bob'])

# # print all the phone entries
# print(phonebook_dict.values())


# nested dictionaries

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

#get the email addres of Ramit
# print(ramit['email'])

#get the first of Ramit's interests
# intr = ramit['interests'][0]
# print(intr)

# get the email address of jasmine
# print(ramit['friends'][0]['email'])

# get the second of Jan's intersts
# print(ramit['friends'][1]['interests'][1])

##### Medium


# word summary
# user_input = input('Please enter a string: ')

# def word_histogram(string):
#   dictionary_of_words = {}
#   list_of_words = string.split()
#   # print(list_of_words)
#   for word in list_of_words:
#     dictionary_of_words[word] = string.count(word)
#   return dictionary_of_words
# print(word_histogram(user_input))



# letter summary

# write a letter histogram program that gets input and prints a dictionary with the tally of how many 
# times each letter in the alphabet was used in the word

# user_input = input('Please enter a word: ')

def letter_histogram(word):
  letters_in_word = {}
  for letter in word:
    letters_in_word[letter] = word.count(letter)
  # for letter in letters_in_word:
  #   print(f'{letter}: {letters_in_word[letter]}')
  return letters_in_word

# print(letter_histogram(user_input))

# sorting a histogram

# def histogram_sort(hist):
#   mylist = []
#   count = 0
#   for item in hist:
#     mylist.append([])
#     mylist[count].append(item)
#     mylist[count].append(hist[item])
#     count += 1
#   highest = mylist[0]
#   for item in mylist:
#     if item[1] > highest[1]:
#       highest = item[1]
#   return (highest)

# print(histogram_sort(letter_histogram(user_input)))

##### large

# phone book app
