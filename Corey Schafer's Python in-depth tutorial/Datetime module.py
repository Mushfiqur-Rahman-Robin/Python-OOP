import datetime
import pytz

d = datetime.date(2022, 2, 3)
print(d)

todayy = datetime.date.today()
print(todayy)
print(todayy.year)
print(todayy.day)

print(todayy.weekday()) # Monday 0, Sunday 6
print(todayy.isoweekday()) # Monday 1, Sunday 7

tdelta = datetime.timedelta(days=7)
print(todayy - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2022,3,25)
till_bday = bday - todayy
print(till_bday)
print(till_bday.total_seconds())

t = datetime.time(9, 30, 40, 5000)
print(t)
print(t.hour)

dt = datetime.datetime(2022,2,3,12,30,21,500)
print(dt)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow) 

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz = pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('Asia/Dacca'))
print(dt_mtn)  # 2022-02-04 09:54:56.312999+06:00

# for tz in pytz.all_timezones:
#     print(tz)

print(dt_mtn.isoformat()) # 2022-02-04 09:54:56.312999+06:00

print(dt_mtn.strftime('%B %d, %Y')) #February 04, 2022
  
# string to datetime

dt_str = 'February 04, 2022'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)  # 2022-02-04 00:00:00