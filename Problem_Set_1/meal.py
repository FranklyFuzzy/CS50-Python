#meal time
#https://cs50.harvard.edu/python/2022/psets/1/meal/
def main():
  z=input('What time is it? ')
  convert(z)


def convert(time):
  time=str(time).replace(':','.')
  time=float(time)
  if 7.00 <= time <= 8.00:
    print('breakfast time')
  elif 12.00 <= time <= 13.00:
    print('Lunch time')
  elif 18.00 <= time <= 19.00:
    print('Dinner time')

if __name__ == "__main__":
    main()

"""
#meal timev2
def main():
  utime=input('What time is it? ')
  tt=convert(utime)
  if 7.00 <= tt <= 8.00:
    print('breakfast time')
  elif 12.00 <= tt <= 13.00:
    print('Lunch time')
  elif 18.00 <= tt <= 19.00:
    print('Dinner time')


def convert(time):
  time=str(time).replace(':','.')
  time=float(time)
  return(time)

if __name__ == "__main__":
    main()
"""
