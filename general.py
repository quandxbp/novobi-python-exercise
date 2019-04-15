import os
from functools import reduce

def readFile(filePath):
    content = ""
    
    if not os.path.isfile(filePath):
        raise FileNotFoundError
    with open(filePath, 'r') as file:
        content = file.read()

    return content
    
def appendTextFile(path, data):
    if not os.path.isfile(path):
        f = open(path, 'w+')
        f.write('')
    with open(path, 'a') as file:
        file.write(data + '\n')


    