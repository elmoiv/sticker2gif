import os
from urllib.request import urlopen, urlretrieve

sep = os.path.sep
ope = os.path.exists

def CheckPath(path):
    if not ope(path):
        path = os.getcwd()
    else:
        if os.path.isfile(path):
            path = os.path.dirname(path)
    if path[-1] != sep:
        path += sep
    return path

def PathOrUrl(inpt):
    # True: path
    # False: url
    # None: nothing
    if ope(inpt):
        return True
    try:
        urlopen(inpt)
    except:
        return None
    return False

def Download(url):
    try:
        urlretrieve(url , 'img.png')
        return 'img.png'
    except:
        raise ConnectionError

def Rename(name, path):
    if not name:
        name = 'Sample'
    for i in os.listdir(path):
        if name + '.gif' == i:
            name += '1'
    return name

def Clean(path):
    p = path + 'temp' + sep
    if not ope(p):
        return
    for i in os.listdir(p):
        os.remove(p+i)
    os.rmdir(p)

def Log(text, switch):
    if switch:
        print(text)