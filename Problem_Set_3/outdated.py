#outdated.py
#https://cs50.harvard.edu/python/2022/psets/3/outdated/#outdated
monthlist =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    udate = input('Date: ')
    if "/" in udate:
        month, day, year = udate.split('/')
    elif "," in udate:
        month, day, year = udate.replace(',','').split()
        if month in monthlist:
            month = monthlist.index(month)
            month+=1
    try:
        if int(day) >= 31 or int(month) >= 12:
            continue
        else:
            break
    except (ValueError,TypeError):
        continue
print(f'{year}-{int(month):02}-{int(day):02}')
