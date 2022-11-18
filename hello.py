def main():
  #assign input to a variable
  name=input("What's your name? ").strip().title() # can add string methods to input straight away

  hello()
  hello(name)

def hello(to="world world"): # assign default value when defining function


  #print with variable
  print("Hello", to)

  # f-string
  print(f'Hello, {to}, but in f-string')

  # remove whitespace from variable
  stripVar="     test      "
  print(f'{stripVar}')
  print(f'Remove white space with "strip()": {stripVar.strip()}')

  # capitalize first letter
  print(f'Capitalize first letter with "capitalize()" {to.capitalize()}')

  print(f'Capitalize all letters with "upper()": {to.upper()}')

  # chain string methods
  print(f'remove white spaces first then capitalize: {stripVar.strip().upper()}')

  # Split user name from first name and last name
  first, last= to.split(" ")
  print(f'First name: {first}')
  print(f'Last name: {last}')

print('We are now going to run hello()')

main()


