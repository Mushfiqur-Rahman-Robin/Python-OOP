language = 'Python'

if language == 'Python':
    print('Language us Python')

elif language == 'Java':
    print('Language is Java')

else:
    print('Other language')

user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('Admin page')
else:
    print('Bad credential')


if user == 'admin' or logged_in:
    print('Admin page')
else:
    print('Bad credential')

if not logged_in:
    print('Please log in')
else:
    print('Welcome')


a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
print(a is b)

condition = {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')