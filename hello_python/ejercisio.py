# name = input('What is your name? ')
# message = f'Hello, {name}'
# print(message)
# letters = len(name)
# new_message = f'your name has {letters} letters in it! awesome'.upper()
# print(new_message)
# import time
# print('let\'s play madlibs')
# time.sleep(2)
# adlib = '__(Proper noun)___ ran __(adverb)__ to the __(noun)__'
# print(adlib)
# proper_noun = input('\n\nProper noun: ')
# print('Got it')
# time.sleep(1)
# adverb = input('Adverb: ')
# print('Got it')
# time.sleep(1)
# noun = input('Noun: ')
# print('Got it')
# time.sleep(1)
# print(f'\n\n {proper_noun} ran {adverb} to the {noun}')
# try:
#     day = int(input('Day (0-6)? '))
#     if day == 0:
#         print('Monday')
#     elif day == 1:
#         print('Tuesday')
#     elif day == 2:
#         print('Wednesday')
#     elif day == 3:
#         print('Thursday')
#     elif day == 4:
#         print('Friday')
#     elif day == 5:
#         print('Saturday')
#     elif day == 6:
#         print('Sunday')
    
# except day > 6:
#     print('Please pick a number 0-6 ')

# day = int(input('Day (0-6)? '))
# if day < 5:
#     print('Go to work')
# else:
#     print('Sleep in')
## C to F ##
# temp = int(input('Temperature in C? '))
# temp = (temp * 1.8) + 32
# print(temp)

# # Tip calculator
# total_bill = input('Total bill amount: ')
# service = input('Level of service (good, fair, bad)? ')
# if service == 'good':
#     tip =total_bill * .2
#     paid = total_bill + tip
# if service == 'fair':
#     tip = total_bill * .15
#     paid = total_bill + tip
# if service == 'bad':
#     tip = total_bill * .1
#     paid = total_bill + tip
# print(f'''\nTotal amount: {total_bill}\nTip: {tip}\n''')

# # splittable tip calculator
total_bill = float(input('Total bill amount: '))
service = input('Level of service (good, fair, bad)? ')
peoples = int(input('How many people? '))

if service == 'good':
    tip = total_bill * .2
    paid = total_bill + tip
if service == 'fair':
    tip = total_bill * .15
    paid = total_bill + tip
if service == 'bad':
    tip = total_bill * .1
    paid = total_bill + tip

final = tip + total_bill
per_person =( float(total_bill) + tip) / peoples
print(f'''\nSubtotal: ${total_bill}\nTip: ${tip}\nTotal: {final}''')
print(f'${per_person} per person\n')

# count to 20 on 0.05s intervals

# import time
# count = 0
# while count <= 20:
#     print(count)
#     time.sleep(.05)
#     count += 1
