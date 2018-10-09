from PIL import Image
import os

class ImageEditor():

    def set_config(self, a):
        self.IMAGE_W = a.IMAGE_W
        self.IMAGE_H = a.IMAGE_H
        self.IMAGE_C = a.IMAGE_C
        self.ROTATE = a.ROTATE
        self.ROTATE_REVERSE = a.ROTATE_REVERSE
        self.WHITE_BLACK = a.WHITE_BLACK

    def __str__(self):
        return f'''
       IMAGE_W = {self.IMAGE_W}
       IMAGE_H = {self.IMAGE_H}
       IMAGE_C = {self.IMAGE_C}
       ROTATE = {self.ROTATE}
       ROTATE_REVERSE = {self.ROTATE_REVERSE}
       WHITE_BLACK = {self.WHITE_BLACK}'''

    def cut(self):
        print('Cutting images')
        for x in os.listdir('media/'):
            i = Image.open(f'media/{x}')
            if self.IMAGE_W in range(1, i.size[0]) or self.IMAGE_H in range(1, i.size[1]):
                if self.IMAGE_C == True:
                    cntr1 = i.size[0] / 2
                    cntr2 = i.size[1] / 2
                    box = (cntr1, cntr2, (cntr1 + self.IMAGE_W), (cntr2 + self.IMAGE_H))
                else:
                    box = (0, 0, self.IMAGE_W, self.IMAGE_H)
                i.crop(box).save(f'media/{x}')

    def roll(self):
        if self.ROTATE in range(1, 360):
            print('Rotating images')
            for x in os.listdir('media/'):
                i = Image.open(f'media/{x}')
                if self.ROTATE_REVERSE == True:
                    i.rotate(360 - self.ROTATE).save(f'media/{x}')
                else:
                    i.rotate(self.ROTATE).save(f'media/{x}')

    def black_n_white(self):
        if self.WHITE_BLACK == True:
            print('Making images black and white')
            for x in os.listdir('media/'):
                i = Image.open(f'media/{x}')
                i.convert(mode='L').save(f'media/{x}')

    def run(self):
        self.cut()
        self.roll()
        self.black_n_white()