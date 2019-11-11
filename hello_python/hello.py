user_number = int(input('Give me a number. '))
try:
    if user_number == 3:
        print('well done')
        quit()
except ValueError:
    print('wrong')
    quit()
    