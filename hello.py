print('Hello world')

#assign input to a variable
name=input("What's your name? ")



#print with variable
print("Hello", name)

# f-string
print(f'Hello, {name}, but in f-string')

# remove whitespace from variable
stripVar="     test      "
print(f'{stripVar}')
print(f'Remove white space with "strip()": {stripVar.strip()}')

# capitalize first letter
print(f'Capitalize first letter with "capitalize()" {name.capitalize()}')

print(f'Capitalize all letters with "upper()": {name.upper()}')

# chain string methods
print(f'remove white spaces first then capitalize: {stripVar.strip().upper()}')