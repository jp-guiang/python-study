def main():
  x=int(input('x: '))
  print(f'x^2 is {square(x)}')

def square(n):
  return n*n

main()

x=int(input('What is x? '))
y=int(input('What is y? '))


print(x+y)

a=float(input('What is a?: '))
b=float(input('What is b?: '))

print(a+b)

c=a+b
c=round(c,2) # Round(number, dp)

print(c)

d=1000
print(f'{d:,}') # use :, to separate numbers with 'z'

e=.066666666
print(f'{e:.2f}') # .2f specify decimal places