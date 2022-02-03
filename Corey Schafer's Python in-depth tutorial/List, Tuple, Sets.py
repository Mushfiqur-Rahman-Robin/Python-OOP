courses = ['CSE-141', 'CSE-241', 'CSE-341', 'CSE-441']
print(len(courses))
print(courses[-2])
print(courses[1])
print(courses[1:4])

courses.append('HUM-141')
print(courses)

# courses.insert(0, 'HUM-141')
# print(courses)

courses_2 = ['CSE-181', 'EE-181']
# courses.insert(4, courses_2)
# print(courses)

courses.extend(courses_2)
print(courses)

courses.remove('HUM-141')
print(courses)

courses.pop() # removes last element of a list
print(courses)

courses.reverse()
print(courses)

courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)

sorted_courses = sorted(courses)
print(sorted_courses)

nums = [1, 4, 6, 2, 5]
print(max(nums))
print(min(nums))
print(sum(nums))

print(nums.index(2))

print(9 in nums)

for index, item in enumerate(courses, start=1):
    print(index, item)

course_str = ', '.join(courses)
print(course_str)

new_list = course_str.split(', ')
print(new_list)

# Lists are mutable, tuples are immutable

""" tuple_1 = ('CSE-441', 'CSE-341', 'CSE-241', 'CSE-181', 'CSE-141')
tuple_2 = tuple_1

tuple_1[0] = 'EE-181'

print(tuple_1) 
print(tuple_2) """

# This code will throw this error: TypeError: 'tuple' object does not support item assignment
# The reason for the error is tuple is immutable.

courses = {'CSE-141', 'CSE-181', 'CSE-241', 'CSE-341', 'CSE-441'}
print(courses)
print('CSE-141' in courses)

eee_courses = {'EEE-141', 'EEE-181', 'CSE-241', 'CSE-341', 'EEE-441'}
print(courses.intersection(eee_courses))

print(courses.difference(eee_courses))

print(courses.union(eee_courses))
