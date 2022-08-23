#fuel.py
#https://cs50.harvard.edu/python/2022/psets/3/fuel/
while True:
  try:
    x,y = input("Fraction: ").split("/")
    z = (int(x)/int(y))
    if z > 1:
      continue
    break
  except(ValueError, ZeroDivisionError):
    pass
    
if z == 1 or z== .99:
  print('F')
elif z == 0 or z == .01:
  print('E')
else:
  print(f'{z:.0%}')
