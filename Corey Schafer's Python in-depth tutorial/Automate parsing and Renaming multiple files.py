import os

os.chdir('D:/Python_Tutorials')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2) # strip from second character of the filenumber
    # fills the number with zero, 2 means two digits: 00, 01, etc.

    new_name = f'{f_num}-{f_title}{f_ext}'
    os.rename(f, new_name)