# Today's algorithms Friday will focus on:
# - Quick review
# - Finding/Reading Documentation
# - Teamwork
# - Pseudo-coding
# - Whiteboarding


# 1.
# Write some code and introduce yourself to your teammates! Use the 'input' function to save everyone's name as a variable so you don't forget 😉
# Create a new variable called my_string set to the string "My name is __name1__ and my teammate's names are __name2__ and __name3__.", with your teammates variables substituted in.  Print my_string

# 2.
#  Uppercase every character in my_string.  Update my_string and print the result.

# 3.
# Count the number of times the letter 'M' occurs in my_string. Print your result. (HINT: google is your best friend.  Strings have built in methods that you can use to easily do seemingly complex things)

# 4.
# Replace all instances of the letter 'A' with the character '4'.  Update my_string and print your result  (String methods :D )

# 5.
# Finish up converting your string into unreadable '90s 13375P34K.  Replace all the following letters with the corresponding numbers:
# L: 1
# E: 3
# T: 7
# S: 5
# O: 0

my_name = input('what is your name? ')
teammate_2 = input('Who is your first team mate? ')
teammate_1 = input('Who is your second team mate? ')
my_string = f'My name is {my_name} and my teammate\'s names are {teammate_1} and {teammate_2}. '
my_string = my_string.upper()
print(my_string)
print(f"there are {my_string.count('M')} 'M's in that string")
print(my_string.replace('A', '4'))
# my_string = my_string.replace('L', '1')
# my_string = my_string.replace('E', '3')
# my_string = my_string.replace('T', '7')
# my_string = my_string.replace('S', '5')
# my_string = my_string.replace('O', '0')
replacement = (
    my_string
        .replace('L', '1')
        .replace('E', '3')
        .replace('T', '7')
        .replace('S', '5')
        .replace('O', '0')
)
print(my_string)
