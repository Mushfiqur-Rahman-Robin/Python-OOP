f = open("../Python+OOP/Corey Schafer's Python in-depth tutorial/test.txt", 'r')
print(f.name)
print(f.mode) # r
f.close()

# using context manager
# automatically closes files after executing the block
with open("../Python+OOP/Corey Schafer's Python in-depth tutorial/test.txt", 'r') as f:
    f_contents = f.read()
    print(f_contents)


with open("../Python+OOP/Corey Schafer's Python in-depth tutorial/test.txt", 'r') as f:
    f_contents = f.readlines()
    print(f_contents)

# ['This is a test file for working with Python file objects.\n', '1. File\n', '2. Files Files\n', '3. Files Files files']

with open("../Python+OOP/Corey Schafer's Python in-depth tutorial/test.txt", 'r') as f:
    f_contents = f.readline()
    print(f_contents, end = '')   

    f_contents = f.readline()
    print(f_contents, end = '')

# This is a test file for working with Python 
# file objects.
# 1. File

with open("../Python+OOP/Corey Schafer's Python in-depth tutorial/test.txt", 'r') as f:
    for line in f:
        print(line, end = '')  # reads the whole file

with open("../Python+OOP/Corey Schafer's Python in-depth tutorial/test.txt", 'r') as f:
    f_contents = f.read(25) 
    print(f_contents, end = '') # reads the first 25 characters


with open("../Python+OOP/Corey Schafer's Python in-depth tutorial/test.txt", 'r') as f:
    size_to_read = 25
    f_contents = f.read(size_to_read) 

    while len(f_contents) > 0:
        print(f_contents, end = '') 
        f_contents = f.read(size_to_read)


# writing files

# with open("C:/Users/USER/Desktop/Project/Python+OOP/Corey Schafer's Python in-depth tutorial/test_write", 'w') as f:
#     f.write('Test write test write test write')


with open("C:/Users/USER/Desktop/Project/Python+OOP/Corey Schafer's Python in-depth tutorial/test.txt", 'r') as rf: 
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# code for working with image files

with open("test.jpg",  'rb') as rf: # in binary mode
    with open('test_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)