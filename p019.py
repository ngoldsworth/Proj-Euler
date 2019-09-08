import datetime as dt

day = dt.date(1900, 1, 1)
num_sundays = 0

while day != dt.date(2000, 1, 1):
    weekday = day.weekday()
    if weekday == 0:
        monthday = day.strftime('%d')
        if monthday == '01':
            num_sundays += 1

    day = day + dt.timedelta(1)

print(num_sundays)