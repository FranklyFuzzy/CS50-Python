#home federal savings bank
#https://cs50.harvard.edu/python/2022/psets/1/bank/
greeting=input()
if greeting.lower().strip().startswith('hello'):
  print("$0")
elif greeting.lower().strip().startswith('h'):
  print("$20")
else:
  print("$100")
