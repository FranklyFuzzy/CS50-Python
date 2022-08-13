#coke.py
#https://cs50.harvard.edu/python/2022/psets/2/coke/
due=50
while due>0:
  print('Amount Due:',due)
  coin = input('Insert Coin: ')
  #This works too:
  #if coin in ["25", "10", "5"]:
  if coin == '25' or coin=='10' or coin=='5':
    due=int(due) - int(coin)
print('Change Owed:', abs(due))
