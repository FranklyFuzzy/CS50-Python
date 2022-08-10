#making faces 
#https://cs50.harvard.edu/python/2022/psets/0/faces/
face=input()
if ':)' in face or ':(' in face:
  print(f'{face.replace(":)","🙂").replace(":(","🙁")}')
