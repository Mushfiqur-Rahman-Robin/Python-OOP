from unittest import result


s1 = set([1, 2, 3, 4, 5])
print(s1)

s1 = set()  # to create an empty set
print(s1)

s1 = {} # creates an empty dictionary

s1 = {1, 2, 3, 4, 5}
s1.add(6)
print(s1)


s1 = {1, 2, 3, 4, 5}
s1.update([6, 7, 8])
print(s1)

s1 = {1, 2, 3, 4, 5}
s2 = {7, 8, 9}
s1.update([6,7,8], s2)
print(s1)


s1 = {1, 2, 3, 4, 5}
s1.remove(5)
print(s1)

s1 = {1, 2, 3, 4, 5}
s1.discard(6)
print(s1)


s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3, 4, 5}

s4 = s1.intersection(s2, s3)
print(s4)


s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3, 4, 5}

s4 = s1.difference(s2)
print(s4)


s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3, 4, 5}

s4 = s1.difference(s1, s3)
print(s4)


#symmetric difference grabs all the difference between two sets

s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3, 4, 5}

s4 = s1.symmetric_difference(s2)
print(s4)


# removing duplicates and return a list

l1 = [1, 2, 3, 1, 2, 3]
l2 = list(set(l1))

print(l2)


employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
gym_members = ['April', 'John', 'Corey']
developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

result = set(gym_members).intersection(developers)  # intersection is a set method. So we had to cast gym_members to set variable before using intersection method
print(result)

result = set(employees).difference(gym_members, developers)  # intersection is a set method. So we had to cast gym_members to set variable before using intersection method
print(result)