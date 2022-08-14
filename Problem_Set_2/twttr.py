#twttr.py
#https://cs50.harvard.edu/python/2022/psets/2/twttr/
"""
I am going to do nested replace method
First thing I did was take 'A','E','I','O','U' and make a list

items=['A','E','I','O','U','a','e','i','o','u']

for i in items:
  print('.replace','(','"',i,'"',',' '"','"',')',sep='', end='')

Output looks like:

.replace("A","").replace("E","").replace("I","").replace("O","").replace("U","").replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")

I then easily assembled my nested replcace methods.
"""
#solution
string = input('Input: ')
rep = string.replace("A","").replace("E","").replace("I","").replace("O","").replace("U","").replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
print('Output:',rep)
