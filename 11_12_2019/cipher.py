# ceaser cipher

playing = True
while playing == True:
    # input: What, which way, how many places?
    target = input("Encrypt this: ")
    direction = (input('Which way would you like to shift? (L/R): ')).lower()
    shift = int(input('How many places would you like to shift? '))
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    def cipher(strang, num, shift):
        index = 0
        final = ''
        # loop through input
        while index < len(strang):
            temp = strang[index]
            index += 1
            #shift to the right'
            try:
                if shift == 'r':
                    if temp == ' ':
                        final += ' '
                    else: 
                        temp = alphabet[(alphabet.index(temp) + num) % 26]
                        final += temp
                #shift to the left
                elif shift == 'l':
                    if temp == ' ':
                        final += ' '
                    else: 
                        temp = alphabet[(alphabet.index(temp) - num) % 26]
                        final += temp
            except ValueError:
                final += temp
        return final

    answer = (cipher(target, shift, direction))
    # print the message
    print(f'''
    Original message: {target}

    Final message: {answer}
    ''')
    keep_playing = (input('Would you like to encrypt anything else? (Y/N) ')).lower()[0]
    valid = False
    while valid == False:
        if keep_playing == 'y':
            playing = True
            valid = True
        elif keep_playing == 'n':
            playing = False
            valid = True
        elif keep_playing != 'y' or 'n':
            keep_playing = input('Please enter a valid selection (y/n) ')
            valid = False
        keep_playing = input('Please enter a valid selection (y/n) ')
    # else: 
    #     print('Play by my rules or don\'t play. ')
    #     playing = False
    
    
print('Goodbye')