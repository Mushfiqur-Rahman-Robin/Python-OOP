import os
from datetime import datetime

os.chdir('C:/Users/USER/Desktop/')

print(os.getcwd())

# os.mkdir('OS-demo')
# os.makedirs('OS-demo/subdir/os')

# os.rmdir('OS-demo')
# os.removedirs('OS-demo/subdir/os')

#os.rename('Vulnerabilites.txt', 'Vulnerabilites of Teletalk.txt')
print(os.stat('Vulnerabilites of Teletalk.txt'))

# print(os.listdir())

mod_time = os.stat('Vulnerabilites of Teletalk.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# for dirpath, dirnames, filenames in os.walk('C:/Users/USER/Desktop/'):
#     print('Current path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()

print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('Home'), 'test.txt')
print(file_path)

print(os.path.split('/tmp/test.txt'))
print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))

print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))  # ('/tmp/test', '.txt')

