# Reading Content of One or More directory
# Structural programming

from os import listdir # Function To list the content in directory
from os.path import join, isdir, isfile

path = r'../../../dec182017'
print(listdir(path))

# To Check absolute path
abs_path = path + "/" + 'ps_datatypes.py'
print(abs_path)

# Checking Absolute Path Using os.path Module
absolute_path = join(path, 'ps_datatypes.py')

print(absolute_path)
print()
print()

print(isdir(absolute_path))
print(isfile(absolute_path))
