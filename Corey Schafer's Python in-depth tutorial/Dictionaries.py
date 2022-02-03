from email.policy import default


student = {'name':'John Doe', 'age' : 30, 'courses' : ['CSE-141', 'CSE-181', 'CSE-241', 'CSE-341', 'CSE-441']}
print(student['name'])
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'Not found!'))
student['phone'] = '0123456789'
print(student.get('phone'))

student.update({'name' : 'Jane', 'age' : 25, 'phone' : '0987654321'})
print(student)

# del student['age']
# print(student)

age = student.pop('age')
print(age)
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)