whole_game = True
while whole_game:
    stil_playing = True

    while stil_playing == True:
        try:
            user_number = int(input('Give me a number '))
            if user_number == 3:
                print('Well done')
                stil_playing = False
            else:
                print('Try again')
        except ValueError:
            print('Please type a number. Thank you. ')
    to_continue = input('Would you like to keep playing? y/n ')
    if to_continue == 'n':
        whole_game = False
    if to_continue == 'y':
        whole_game = True