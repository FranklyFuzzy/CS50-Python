#making faces
face=input()
if ':)' in face or ':(' in face:
  print(f'{face.replace(":)","🙂").replace(":(","🙁")}')
