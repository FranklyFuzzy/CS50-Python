#deep
#https://cs50.harvard.edu/python/2022/psets/1/deep/
deep = input('What is the Answer to the Great Question of Life, the Universe and Everything? ')
if '42' in deep or 'forty-two' in deep.lower() or 'forty two' in deep.lower():
  print('Yes')
else:
  print('No')

#this works too
if deep.strip()=='42' or deep.strip().lower()=='forty-two' or deep.strip().lower()=='forty two':
  print('Yes')
else:
  print('No')
