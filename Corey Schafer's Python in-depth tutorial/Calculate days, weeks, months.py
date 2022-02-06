import datetime
import calendar

balance = 5000
interest_rate = 10*0.1
monthly_payment = 500

today = datetime.date.today()

days_in_current_month = calendar.monthrange(today.year, today.month)[1]
# returns a tuple with the day of the week that the first of that month falls on
# and how many days are in that month

#print(days_in_current_month)  # 28

days_in_end_month = days_in_current_month - today.day
#print(days_in_end_month) #22

start_date = today + datetime.timedelta(days = days_in_end_month + 1)
#print(start_date)  # 2022-03-01
end_date = start_date

while balance > 0:
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= monthly_payment
    balance = round(balance, 2)

    if balance < 0:
        balance = 0

    print(end_date, balance)

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days = days_in_current_month)



# how many weeks it will need to lose certain amount of pounds

import datetime

current_weight = 220
goal_weight = 180
avg_lbs_week = 1.5

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days = 7)
    current_weight -= avg_lbs_week

print(f'Reached targeted goal in {(end_date - start_date).days // 7} weeks')  # // returns decimal value
# end_date - start_date returns a timedelta
print(end_date)


# How long to reach a certain amount of subscriber in YouTube

import datetime
import math

goal_subs = 1000000
current_subs = 885000

subs_to_go = goal_subs - current_subs

avg_subs_per_day = 3500

days_to_go = math.ceil(subs_to_go / avg_subs_per_day)
today = datetime.date.today()

print(today + datetime.timedelta(days=days_to_go))



