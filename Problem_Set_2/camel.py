#camel.py
#https://cs50.harvard.edu/python/2022/psets/2/camel/
camel = input('camelCase: ')
snake=''
for i in camel:
  if i.isupper():
    snake=snake + '_' + i
  else:
    snake += i
print(snake.lower())
