class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
    
    def __repr__(self):  # Unambiguous representation of the object
                         # Used for debugging, logging, etc. Meant to be seen by other developers
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
        
    def __str__(self):  # Readable representation of an object 
                        # Meant to be used a display to the end user
        return "{} - {}".format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
    
emp_1 = Employee('Mushfiqur', 'Rahman', 25000)
emp_2 = Employee('Unknown', 'User', 15000)

print(emp_1 + emp_2)

#print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(int.__add__(1,2))
# print(str.__add__('a', 'b'))

# print(len('test'))
# print('test'.__len__())

print(len(emp_1))