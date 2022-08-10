#extension.py
#https://cs50.harvard.edu/python/2022/psets/1/extensions/
x=input('File name: ')
x=x.lower()
if x.endswith(('.gif','.jpg','.jpeg','.png')):
  x=x.split('.')
  print('image/'+x[1])
elif x.endswith(('.pdf','.zip')):
  x=x.split('.')
  print('application/'+x[1])
elif x.endswith(('.txt')):
  print('text/plain')
else:
  print('application/octet-stream')
