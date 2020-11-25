import datetime
import datetime
print ( dir(datetime))

from datetime import datetime, time, date, timedelta
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp= now.timestamp()
print(day,month,year,hour,minute,second)
print(timestamp, timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')


# formating date output using striftime
new_year = datetime(2020,1,1)
print(new_year)

day = new_year.day
new_month = new_year.month
ne_year = new_year.year
new_hour = new_year.hour
new_minute = new_year.minute
new_second = new_year.second
print(new_month, ne_year, new_hour,new_minute, new_second)
print(f'{day}/{new_month}/{new_year}, {new_hour}:{new_minute}:{new_second}')

# Time formatting
# 1.current date & time
current_date = datetime.now()
t= now.strftime("%H:%M:%S")
print("Time:", t)

time_one = now.strftime("%m/%d/%Y,  %H:%M:%S")
print("Time one: ", time_one)

time_two = now.strftime("%d/%m/%Y,  %H:%M:%S")
print("Time Two: ", time_two)

# String to time using strptime
date_string = "25 November, 2020"
print("Date String", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Date object =" ,date_object)

# Using date from datetime

a = time()
print("a =", a)
b= time(10,30,50)
print("b=", b)
c= time(hour=3, minute=34, second=59)
print("C =", c)
d= time(10,30,50, 200555)
print("D =", d)

# Different between two points in time
today = date(year=2020, month=11, day=25)
new_year2021 = date(year=2021, month=1, day=1)
time_left_for_new_year = new_year2021- today
print(time_left_for_new_year)

t1= datetime(year=2020, month=11,day=25,hour=12,minute=34,second=57)
t2 = datetime(year=2021, month=1,day=1,hour=12,minute=23,second=30)
diffrence = t2-t1
print(diffrence)

# Difference between two points in time using timedelta
time1 = timedelta(weeks=12,days=30,hours=5,seconds=35)
time2 = timedelta(weeks=7,hours=4,minutes=45,seconds=45)
time3 = time1-time2
print("Time 3=", time3)

