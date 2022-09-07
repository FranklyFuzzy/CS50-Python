#grocery.py
#https://cs50.harvard.edu/python/2022/psets/3/grocery/
grocery = {}
while True:
    try:
      item = input().upper()
      if item in grocery:
        grocery[item] += 1
      else:
        grocery[item] = 1
    except EOFError:
        print()
        break

for i in sorted(grocery):
	print(i, grocery[i])
