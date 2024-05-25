import calendar
from calendar import Calendar

# for years 
print(calendar.calendar(2018))
    
#for specific month of the year
mm=3
print(calendar.month(2018,mm))

# now we have some iterative function of the 
obj=Calendar()   #for months
for i in obj.itermonthdays(2018,9):
    print(i)
    
#for weeks(simply print days)
obj=Calendar()
for i in obj.iterweekdays():
    print(i)
#other(in that case the output is in tuple form)(1-represent the date)(2-represent the day on that date)
#(in date 0 represent date of previous calender)(2-in day 0 is for monday and 6 is for sunday)
obj=Calendar()
for i in obj.itermonthdays2(2023,7):
    print(i)
    
#other(in that case the output is in tuple)(1-value represent the year)(2-month)(3-date)
obj=Calendar()
for i in obj.itermonthdays3(2022,7):
    print(i)
#other(also show output in tuple)(1-year)(2-month)(3-date)(4-days)
obj=Calendar()
for i in obj.itermonthdays4(2023,6):
    print(i)
#display simply week first day that is monday
obj = Calendar()
first_weekday = obj.getfirstweekday()
print(first_weekday)
obj=Calendar()
obj.