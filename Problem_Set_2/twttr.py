#twttr.py
#https://cs50.harvard.edu/python/2022/psets/2/twttr/
"""
I am going to do nested replace method
First thing I did was take 'A','E','I','O','U' and make a list.  items=['A','E','I','O','U']
Then i need to make them lower

items2=[x.lower() for x in items]

for i in items2:
  print('.replace','(','"',i,'"',',' '"','"',')',sep='')

.replace("a","")
.replace("e","")
.replace("i","")
.replace("o","")
.replace("u","")

I then easily assembled my nested replcace methods.
"""
#solution
string = input('Input: ')
rep = string.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
print('Output: ',rep, sep='')
