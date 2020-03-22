from itertools import groupby

class Brain:
    def __init__(self, image):
        self.image = image
        
    def detect(self, rgb_img, x, y, i):
        for pixelX in range(0, x):

            # Pixel data will store sum of pixels colors in each line
            pixel_data = []
            for pixelY in range(y):

                # If i == -1 then we reverse the points (When we want to scan horizontal instead of vertical lines)
                point = (pixelX, pixelY)[::i]

                # Sum of (r, g, b) for each pixel
                rgb_sum = sum(rgb_img.getpixel(point))
                pixel_data.append(rgb_sum)

            # Checks if this line is transparent or contains colors
            # If True we yield 1 else 0
            detect = sum(pixel_data)
            
            if detect:
                yield 1
            else:
                yield 0

    def run(self):
        width, height = self.image.size

        rgbImage = self.image.convert('RGB')
    
        wd = self.detect(rgbImage, width, height, 1)
        ht = self.detect(rgbImage, height, width, -1)

        w = [i[0] for i in groupby(wd) if i[0]]
        h = [i[0] for i in groupby(ht) if i[0]]

        return sum(w), sum(h)
