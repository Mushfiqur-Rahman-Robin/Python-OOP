message = 'Hello world'
print(message.upper())
print(message.lower())
print(message.count('o'))
print(message.find('l'))
print(message[0:5])
message = message.replace('World', 'Universe')
print(message)

greeting = 'Hello'
name = 'User'

message = greeting + ' ' + name
print(message)

message = '{} {}'.format(greeting, name)
print(message)

message = f'{greeting} {name}'
print(message)

print(dir(message)) 
print(help(str.lower))