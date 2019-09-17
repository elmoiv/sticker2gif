import os, ai
from PIL import Image
from tools import *

class StickertoGif:
    def __init__(self, img_path, save_path, log=False):
        self.img_path = img_path
        self.path = CheckPath(save_path)
        self.log = log
        Clean(self.path)
        os.chdir(self.path)
        os.makedirs('temp', exist_ok=True)
        os.chdir('temp')

    def getImg(self):
        choice = PathOrUrl(self.img_path)
        img = None
        if choice:
            img = self.img_path
        elif choice is False:
            Log('\nDownloading...', self.log)
            img = Download(self.img_path)
        else:
            raise Exception('Invalid Image input!')
        return Image.open(img)
            

    def cutImg(self):
        sticker = self.getImg()

        size = sticker.size

        # Using basic AI to determine mini images in each row and column
        Log('\nAI Running...', self.log)
        AI = ai.Brain(sticker)
        columns, rows = AI.run()
        Log('\nRows: {}, Columns: {}'.format(rows, columns), self.log)

        # Getting the fixed size of each mini image
        x, y = round(size[0]/columns), round(size[1]/rows)

        # Setting up cordinates
        cd = (0, 0, x, y)

        Log('\nCutting process...', self.log)
        n = 0
        for _ in range(rows):

            for _ in range(columns):

                # Cropping the mini image
                minSticker = sticker.crop(cd)
                
                colors = minSticker.convert('RGB').getcolors()
                if colors == None:
                    colors = [(0, (1, 0, 0))]
                
                # Detecting empty mini images and bypassing them
                if not (sum(colors[0][1]) == 0 and len(colors) == 1):
                    # minSticker.mode = RGBA so that we create a white background
                    # of same mode to avoid black background when converting to gif
                    Image.alpha_composite(Image.new('RGBA', (x, y), (255, 255, 255)), minSticker).save(str(n) + '.png')
                    n += 1
                
                # Cordinates of the next image in same row
                cd = (cd[0] + x, cd[1], cd[2] + x, cd[3])
            
            # Cordinates of the first image in the next row
            cd = (0, cd[1] + y, x, cd[3] + y)

    def gifImg(self, name, duration):
        pics = [i for i in os.listdir() if i.split('.')[0].isdecimal()]
        
        # Sorting pics ascendingly
        pics.sort(key = lambda x: int(x.split('.')[0]))

        frames = []
        for i in pics:
            frame = Image.open(i)
            frames.append(frame)
        
        # Return to main dic
        os.chdir(os.getcwd()[:-4])

        # Correct any incorrect input
        name = Rename(name, self.path)

        # Catch Stupid Inputs
        try:
            duri = int(duration)
            if not 0 < duri < 101:
                duri = 60
        except:
            duri = 60
        
        # Create GIF
        Log('\nCreating Gif...', self.log)
        frames[0].save(name + '.gif',
                    save_all = True,
                    append_images = frames[1:],
                    duration = duri,
                    loop = 0)

    def run(self):
        self.cutImg()
        self.gifImg(input('\nGIF name: '), input('\nDuration [from 1 to 100]: '))
        Clean(self.path)
        Log('\nDone!', self.log)
