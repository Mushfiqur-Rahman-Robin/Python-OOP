import Importing_modules as module
courses = ['CSE-141', 'CSE-181', 'CSE-241', 'CSE-341', 'CSE-441']

index =  module.find_index(courses, 'CSE-341')
print(index)

from Importing_modules import find_index, test
index =  find_index(courses, 'CSE-341')
print(index)
print(test)

import sys
# print(sys.path)

import random
random_course = random.choice(courses)
print(random_course)

import math 
rads = math.radians(90)
print(rads)

import datetime
today = datetime.date.today()
print(today)

import calendar
print(calendar.isleap(2017))

import os
print(os.getcwd()) # get current working directory


