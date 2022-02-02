from numpy import full


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Name DELETED!')
        self.first = None
        self.last = None

    
emp_1 = Employee('Unknown', 'User', 15000)
#emp_1.first = 'Known'

emp_1.fullname = 'Mushfiqur Rahman'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

