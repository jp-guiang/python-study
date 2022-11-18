def hello():

  #assign input to a variable
  name=input("What's your name? ").strip().title() # can add string methods to input straight away

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

  # Split user name from first name and last name
  first, last= name.split(" ")
  print(f'First name: {first}')
  print(f'Last name: {last}')

print('Hello world')

print('We are now going to run hello()')

hello()

