print('Hello world')

#assign input to a variable
name=input("What's your name? ")



#print with variable
print("Hello", name)

# f-string
print(f'Hello, {name}, but in f-string')

# remove whitespace from variable
stripVar="     test      "
stripVar=stripVar.strip()
print(f'This variable should have no extra white space: {stripVar}')