<<<<<<< HEAD
import datetime, time, calendar
bday = datetime.date(1992, 4, 8)
nbday = datetime.date(2020, 4, 8)
tday = datetime.date.today()
till_nbday = nbday - tday
dt_now = datetime.datetime.now()
tdelta = datetime.timedelta(hours = 24)
print(bday, '\n')
print(bday.year, '\n')
print(bday.month, '\n')
print(bday.day, '\n')
print(bday.isoweekday(), '\n')
print(till_nbday, '\n')
print(calendar.month(2017, 5), '\n')
print('Yesterday:', dt_now - tdelta, '\n')
print('One day after yesterday:', dt_now + tdelta, '\n')
=======
import datetime, time, calendar
bday = datetime.date(1992, 4, 8)
nbday = datetime.date(2020, 4, 8)
tday = datetime.date.today()
till_nbday = nbday - tday
dt_now = datetime.datetime.now()
tdelta = datetime.timedelta(hours = 24)
print(bday, '\n')
print(bday.year, '\n')
print(bday.month, '\n')
print(bday.day, '\n')
print(bday.isoweekday(), '\n')
print(till_nbday, '\n')
print(calendar.month(2017, 5), '\n')
print('Yesterday:', dt_now - tdelta, '\n')
print('One day after yesterday:', dt_now + tdelta, '\n')
>>>>>>> 90b5633f9bd6f57998b6a7f286d2af33b42f15fc
print('Three days before yesterday:', dt_now - 4*tdelta, '\n')