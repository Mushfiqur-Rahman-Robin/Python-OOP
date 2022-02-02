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

print(Employee.number_of_employee)

emp_1 = Employee('Mushfiqur', 'Rahman', 25000)
emp_2 = Employee('Unknown', 'User', 15000)

#print(emp_1.fullname())  # When working with methods on an instance we don't have to take that instance as an argument

#print(Employee.fullname(emp_1)) # When working with class we have to pass the instance

#print(emp_1.__dict__)

#Employee.raise_amount = 1.05
#emp_1.raise_amount = 1.05

#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

print(Employee.number_of_employee)