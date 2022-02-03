def hello_func(greeting):
    return f'{greeting} Function.'

# print(hello_func())
# print(hello_func().upper())

print(hello_func('Hey'))

def hello_func(greeting, name = 'You'):
    return f'{greeting} {name} Function.'

print(hello_func('Hi', 'Mr.'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

#student_info('Math', 'Science', name = 'John', age = 25)

courses = ['Math', 'Science']
info = {'name': 'John', 'age': 25}

student_info(*courses, **info)


month_days = [0, 31, 28, 31, 30, 31,  30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year%4 == 0 and (year%100!= 0 or year%400 == 0)

def days_in_month(year, month):
    if not 1<=month<=12:
        return 'Invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2017, 2))    