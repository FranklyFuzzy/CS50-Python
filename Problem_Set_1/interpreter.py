#Math Interpreter
#https://cs50.harvard.edu/python/2022/psets/1/interpreter/
x, y, z = input('Expression: ').split(" ")

x=float(x)
z=float(z)

if y=='+':
  print(x+z)
if y=='-':
  print(x-z)
if y=='*':
  print(x*z)
if y=='/':
  print(round(x/z,1))
