from calendar import c


li = [2,1,5,9,8,4,3,7,10,6]
sorted_li = sorted(li)
print(sorted_li)

li.sort() # sorts original list
print(li)

# sorted function returns new sorted list
# sort method sorts in place and returns None
# sort method only works on list

sorted_li = sorted(li, reverse=True)
print(sorted_li)

li.sort(reverse=True)
print(li)

# sorting tuples
tup = (2,1,5,9,8,4,3,7,10,6)
sorted_tup = sorted(tup)
print(sorted_tup)

# sorting dictionaries

dic = {'name':'unknown', 'job':'coding', 'age': 25, 'os': 'windows'}
sorted_dic = sorted(dic)
print(sorted_dic)

# sorting with absolute values
li = [-6, -4, 1, 3, 2, -5]
srted_li = sorted(li, key = abs)
print(srted_li)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'({self.name}, {self.age}, {self.salary}) '

e1 = Employee('a', 25, 10000)
e2 = Employee('x', 35, 30000)
e3 = Employee('m', 28, 15000)

employees = [e1, e2, e3]

def emp_sort(emp):
    return emp.salary

sort_employees = sorted(employees, key = emp_sort)
print(sort_employees)

sort_employees = sorted(employees, key = lambda e: e.salary)  # with lambda function
print(sort_employees)

from operator import attrgetter
sort_employees = sorted(employees, key = attrgetter('salary'))  # with attrgetter
print(sort_employees)