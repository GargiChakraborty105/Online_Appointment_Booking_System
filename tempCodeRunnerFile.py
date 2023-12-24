import datetime
date =datetime.date.today()
day = str(date.day+1)
month = str(date.month)
year = str(date.year)
# date = str(date)[-2:]
print(f"{day}/{month}/{year}")