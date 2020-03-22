import os, shutil
from urllib.request import urlopen, urlretrieve

sep = os.path.sep
ope = os.path.exists
opj = os.path.join

def PathOrUrl(inpt):
    # If path return True else it is assumed a url
    if ope(inpt):
        return True
    try:
        urlopen(inpt)
    except:
        raise TypeError('Boolean Required!')
    return False

def Download(url):
    pic = 'temp\\img.png'
    try:
        urlretrieve(url , pic)
        return pic
    except:
        raise ConnectionError

def Rename(name):
    if not name:
        name = 'Sample'

    for i in os.listdir():
        if name + '.gif' == i:
            name += '1'
    
    return name

def Clean():
    try:
        shutil.rmtree('temp')
    except:
        pass

def Log(text, switch):
    if switch:
        print(text)
