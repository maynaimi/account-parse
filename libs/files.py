import os

def listFiles():
    return os.listdir(_getFilesDirectory())

def readFile(fileName):
    with open (_getFilesDirectory() + '/' + fileName) as f:
        content = f.readlines()

    content = [x.strip() for x in content] 
    return content

def writeFile():
    return None

def _getFilesDirectory():
    cwd = os.getcwd()
    return cwd + '/Files/'


