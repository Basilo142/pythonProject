import calendar
#c=calendar.Calendar(0)

#print(c.monthdays2calendar(2020,10))
calText= calendar.TextCalendar()
print(calText.formatmonth(2021, 8))
#c = calendar.HTMLCalendar(0)
#print(c.formatmonth(2020,10))
print(calendar.isleap(2021))
print(calendar.weekday(2022, 4, 21))
