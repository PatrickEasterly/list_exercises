# variable names in python have underscores
# snake_case , not camelCase
user_name = input('What is your name? ')

#string substitution (interpolation)
# 1. A string with *placeholders*
# 2. the interpolation operator (%)
# 3. values to interpolate into the string
# ##if interpolating a single value, you don't need parens of a comma

greeting = "Hello, %s!" % user_name
# # if interpolating multiples, use parentheses and commas


greeting = f'hello, {user_name}!'
print(greeting.upper())