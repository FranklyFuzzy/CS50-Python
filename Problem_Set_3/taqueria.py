#taqueria.py
#https://cs50.harvard.edu/python/2022/psets/3/taqueria/
menu={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total=0

while True:
  try:
    order=input('Item: ')
    order=order.lower()
    if order == "":
      break
    for item in menu:
      if order in item.lower():
        food,price = item, menu[item]
        if food.lower() == order:
          total += price
          print(f'${total:.2f}')
  except EOFError:
    break
