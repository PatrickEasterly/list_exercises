# count down from 10 (andy)
# count down, but no more than 20
# import time
# count = int(input('Set the timer for no more than 20 seconds: '))
# if count > 20:
#     print('No more than 20!!\n')
#     count = int(input('Set the timer for no more than 20 seconds: '))

# while count != -1:
#     print(count)
#     time.sleep(1)
#     count -= 1
# import random

# secret_number = random.randint(1, 10)
# print("I am thinking of a number between 1 and 10")
# playing = True
# while playing:
#     answer = int(input("What's the number? "))
#     if answer > secret_number:
#         print(f'{answer} is too high')
#     elif answer < secret_number:
#         print(f'{answer} is too low')
#     elif answer == secret_number:
#         print('Yes! You win! ')
#         playing = False

# limited number of guesses, with hints
import random

secret_number = random.randint(1, 10)

still_playing = True
playing = True
guesses = 5
while still_playing == True:
    while playing == True:
        print('I am thinking of a number between 1 and 10')
        answer = int(input('What is your guess? '))
        if answer < secret_number:
            guesses -= 1
            print(f'{answer} is too low, try again. \nYou have {guesses} guesses left')
            
        elif answer > secret_number:
            guesses -= 1
            print(f'{answer} is too high, try again. \nYou have {guesses} guesses left')
            
        else: 
            print('Yes! You win! ')
            playing = False
    
    will_keep_playing = input('Would you like to keep playing? (y/n) ')
    if will_keep_playing == 'y':
        playing = True
        guesses = 5
    else:
        playing = False
        still_playing = False
print('Goodbye')