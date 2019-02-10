#       sticker2gif.py, a Facebook messenger animated sticker downloader
#
#       Copyright 2019 Khaled El-Morshedy <elmoiv>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License 3 as published by
#       the Free Software Foundation.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import os, urllib.request, sys
from PIL import Image

def GetImg():
    try:
        urllib.request.urlretrieve(input('URL: ') , 'img.png')
    except:
        # I am too lazy to catch each error ~(o.o)~
        input('Bad Link!')
        sys.exit()

def AI(test):
    lst = [[], []]
    width, height = test.size
    nTest = test.convert('RGB')
    for w in range(0, width, 10):
        lstWH = []
        for wh in range(height):
            lstWH.append(sum(nTest.getpixel((w, wh))))
        detect = int(''.join(str(i) for i in lstWH))
        if detect == 0: lst[0].append('^')
        else:   lst[0].append('_')
    for h in range(0, height, 10):
        lstHW = []
        for hw in range(width):
            lstHW.append(sum(nTest.getpixel((hw, h))))
        detect = int(''.join(str(i) for i in lstHW))
        if detect == 0: lst[1].append('^')
        else:   lst[1].append('_')
    return [len([x for x in ''.join(lst[lst.index(i)]).split('_') if x != '']) - 1 for i in lst]

def CutImg():
    sticker = Image.open('img.png')
    size = sticker.size
    # Using basic AI to determine mini images in each row and column
    wd_pc, ht_pc = AI(sticker)
    # Getting the fixed size of each mini image
    x, y = round(size[0]/wd_pc), round(size[1]/ht_pc)
    # Setting up cordinates
    cd = (0, 0, x, y)
    n = 0
    for _ in range(ht_pc):
        for _ in range(wd_pc):
            # Cropping the mini image
            minSticker = sticker.crop(cd)
            colors = minSticker.convert('RGB').getcolors()
            if colors == None:
                colors = [(0, (1, 0, 0))]
            # Detecting empty mini images
            if not (sum(colors[0][1]) == 0 and len(colors) == 1):
                # minSticker.mode = RGBA so that we create a white background
                # of same mode to avoid black background when converting to gif
                Image.alpha_composite(Image.new('RGBA', (x, y), (255, 255, 255)), minSticker).save(str(n) + '.png')
                n += 1
            # Cordinates of the next image in same row
            cd = (cd[0] + x, cd[1], cd[2] + x, cd[3])
        # Cordinates of the first image in the next row
        cd = (0, cd[1] + y, x, cd[3] + y)

def GifImg():
    pics = [i for i in os.listdir() if i.split('.')[0].isdecimal()]
    pics.sort(key = lambda x: int(x.split('.')[0]))
    frames = []
    for i in pics:
        frame = Image.open(i)
        frames.append(frame)
    name = input('Sticker Name: ')
    duri = int(input('Duration [1-100]: '))
    frames[0].save(name + '.gif',
                save_all = True,
                append_images = frames[1:],
                duration = duri,
                loop = 0)

def Clean():
    for i in os.listdir('temp\\'):
        if not i.endswith('.gif'):
            os.remove(i)
    os.rmdir('temp\\')

def Main():
    gifDir = 'Sticker2Gif\\'
    if not os.path.exists(gifDir):
        os.mkdir(gifDir)
    os.chdir(gifDir)
    if not os.path.exists('temp\\'):
        os.mkdir('temp\\')
    GetImg()
    CutImg()
    GifImg()
    Clean()
    input('Done!')

Main()