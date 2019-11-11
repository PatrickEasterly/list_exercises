whole_game = True
while whole_game:
    still_playing = True
    while still_playing:
        try:
            user_num = int(input('Give me a number! '))
            if user_num > 5:
                print('Too high! ')
            elif user_num == 5:
                print('You guessed right! ')
                still_playing = False
            else:
                print('Too low! ')
        except ValueError:
            print('Please enter a number. ')
    play_again = input('Would you like to play again? [y/n]' )
    if play_again == 'y':
        whole_game = True
    elif whole_game == 'n:
        whole_game = False
    else: 
        print('Please type "y" or "n" ')