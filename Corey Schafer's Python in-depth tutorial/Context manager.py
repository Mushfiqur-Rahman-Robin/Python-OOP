
class Open_file():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exe_type, exe_val, traceback):
        self.file.close()

with Open_file('sample.txt', 'w') as f:
    f.write('testing')

#print(f.closed)   # True


# context manager using function


from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

with open_file('sample.txt', 'w') as f:
    f.write('testing')

#print(f.closed)


import os
from contextlib import contextmanager

cwd = os.getcwd()
os.chdir(r"C:\Users\USER\Desktop\Project\Python+OOP\Corey Schafer Python-OOP")
print(os.listdir())

cwd = os.getcwd()
os.chdir(r"C:\Users\USER\Desktop\Project\Python+OOP\Corey Schafer's Python in-depth tutorial")
print(os.listdir())




@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir(r"C:\Users\USER\Desktop\Project\Python+OOP\Corey Schafer's Python in-depth tutorial"):
    print(os.listdir())

with change_dir(r"C:\Users\USER\Desktop\Project\Python+OOP\Corey Schafer Python-OOP"):
    print(os.listdir())
