import os

file_name = 'resource/text.tx'

try:
    file = open(file_name)
    print('File found')
except FileNotFoundError:
    print('File is not found')
