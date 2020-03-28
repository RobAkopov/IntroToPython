import datetime
from datetime import timedelta
dt = datetime.date.today()
num_y = int(input('Input years: '))
num_d = int(input('Input days: '))
num_y = num_y*365
num_all_d = num_y + num_d
tdelta = datetime.timedelta(days = num_all_d)
print('Current date:', dt)
print('Given years:', int(num_y/365))
print('Given days:', num_d)
print('Final date:', dt + tdelta)
