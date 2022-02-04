nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []

for n in nums:
    my_list.append(n)
print(my_list)

# using list comprehension in stead of using this loop

my_list = [n for n in nums]
print(my_list)

my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

# using list comprehension in stead of using this loop
my_list = [n*n for n in nums]
print(my_list)

# Using a map + lambda

# map runs everything through a certain function
# lambda is an anonymous function
my_list =  map(lambda n: n*n, nums)
print(my_list)

# n for each n in nums if n is even
my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)

# using list comprehesion for the above code
my_list = [n for n in nums if n%2 == 0]
print(my_list)

# using filter + lambda 
my_list =  filter(lambda n: n%2 == 0, nums)
print(my_list)

# a (letter, number) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)

# using list comprehension
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# dictionary coprehensions
names = ['bruce', 'clark', 'peter', 'logan', 'wade']
heroes = ['batman', 'superman', 'spiderman', 'wolverine', 'deadpool']

# a dict {'name' : 'hero'} for each name, hero in zip(names, heroes)

my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero
print(my_dict)

# using dictionary comprehension
my_dict = {name:hero for name, hero in zip(names, heroes)}
print(my_dict)

my_dict = {name:hero for name, hero in zip(names, heroes) if name!= 'peter'}
print(my_dict)

nums = [1,1,3,1,2,3,5,6,4,6,7,9,9,8]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

# using list comprehension
my_set = {n for n in nums}
print(my_set)

# generator expressions
# yield n*n for each n in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n
my_gen = gen_func(nums)

for i in my_gen:
    print(i)

my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)



