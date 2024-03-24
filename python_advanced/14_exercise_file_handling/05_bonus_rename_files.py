import os
import re


def refactoring(dir_name):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            new_name = filename.lower()
            new_file = '/'.join(re.split(r'[\\/]', file)[:-1]) + '/' + new_name
            os.rename(file, new_file)
        elif os.path.isdir(file):
            refactoring(file)


directory = input('Enter a directory: ')
refactoring(directory)
