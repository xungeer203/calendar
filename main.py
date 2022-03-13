"""
打印指定年份的月历
"""

import calendar
import csv

# class CustomHTMLCal(calendar.HTMLCalendar):
#     cssclasses = ["日","一","二","三","四","五","六"]

# yy = 2014  # year
# mm = 11  # month

# output = calendar.month(yy,mm)
# print(output)
# print(output[45:80])

# mycalendar = calendar.TextCalendar()
# output2 = mycalendar.formatyear(theyear=yy, m=4)
# print(output2)

# with open("mycalendar.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerow(output2)

mycalendar2 = calendar.HTMLCalendar(firstweekday=6)
# mycalendar2 = CustomHTMLCal()

for yy in range(2000, 2024):
    output3 = mycalendar2.formatyear(theyear=yy, width=4)
    # output3 = mycalendar2.formatmonth(theyear=yy, themonth=1,withyear=True)
    print(output3)


# mycalendar3 =

# print(type(calendar.month(yy,mm)))



