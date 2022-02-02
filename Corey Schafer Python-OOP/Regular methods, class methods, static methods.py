from os import stat


class Employee:
    number_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.number_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Mushfiqur', 'Rahman', 25000)
emp_2 = Employee('Unknown', 'User', 15000)

emp_string_1 = 'John-Doe-70000'
emp_string_2 = 'Steve-Smith-30000'
emp_string_3 = 'Jane-Doe-50000'

new_emp_1 = Employee.from_string(emp_string_1)

#Employee.set_raise_amount(1.05)

#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2022, 2, 1)
print(Employee.is_workday(my_date))