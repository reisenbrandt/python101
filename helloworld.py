# Print strings with quotes
print('Hello World')
print("Hello World")
# Print multiline strings with tripe quotes
print('''Hello World''')
print("""
Hello
My name is Rachel
World
""")

# Putting a \ before a character - called escaping 
# Interpret the next character as a character and 
# not as a marker for the string
print("Hello \"the\" World")

# Concatenate using +
print('Hello World,' + ' What\'s up?')

# Numbers have no quotes
# Can not concat strings and numbers - numbers need to be
# strings using str()
print('The result of 1 + 2 is ' + str(1 + 2))


# integer - whole number
print(1)

# float - fractional number
print(2.2)

# prints a whole number but calculates as float
print(1 + 2.0)

# variable = value
name = 'Rachel'

# cannot name a variable with a reserved word
# False - await - else - import - pass
# none - break - except - in - raise
# true - class - finally - is - return

# snakecase - in python, words are connected with underscores
# can not start a variable name with a number
first_name = 'Rachel'
print(first_name)

print('Hello, ' + first_name)

# numbers can be assigned to variables too
first_number = 10
second_number = 20

# variables can store the result of any expressions
the_answer = first_number + second_number
print(the_answer) # 30



