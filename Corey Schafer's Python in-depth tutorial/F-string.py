from datetime import datetime


first_name = 'Unknown'
last_name = 'User'

sentence = 'My name is {} {}'.format(first_name, last_name)
print(sentence)

sentence = f'My name is {first_name} {last_name}'
print(sentence)

person = {'name':'unknown', 'age':24}

sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
print(sentence)

sentence = f"My name is {person['name']} and I am {person['age']} years old."
print(sentence)

calc = f'4 times 11 is {4 * 11}'
print(calc)


for n in range(1,11):
    num = f'The number is {n:02}'  # zero padding with two digits
    print(num)

pi = 3.14159265

sentence = f'Pi is equal to {pi:.4f}' # to print 4 digits after decimal point
print(sentence)

birthday = datetime(1990,2,2)
sentence = f'John has a birthday on {birthday:%B %d, %Y}'
print(sentence)