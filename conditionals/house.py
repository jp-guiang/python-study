name = input("What's your name?: ")

match name:
  case 'Harry' | 'Hermione' | 'Ron':
    print('Gryff')
  case 'Draco':
    print('Slyth')
  case _:
    print('Ayeeee?')