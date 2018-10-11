from PIL import Image
import os


class ImageEditor:

    def set_config(self, config_atts):
        self.config = config_atts

    def __str__(self):
        return f'''
       IMAGE_W = {self.config.IMAGE_W}
       IMAGE_H = {self.config.IMAGE_H}
       IMAGE_C = {self.config.IMAGE_C}
       ROTATE = {self.config.ROTATE}
       ROTATE_REVERSE = {self.config.ROTATE_REVERSE}
       WHITE_BLACK = {self.config.WHITE_BLACK}'''

    def cut(self, i):
        if self.config.IMAGE_W in range(1, i.size[0]) or self.config.IMAGE_H in range(1, i.size[1]):
            if self.config.IMAGE_C is True:
                cntr1 = i.size[0] / 2
                cntr2 = i.size[1] / 2
                return i.crop((cntr1, cntr2, (cntr1 + self.config.IMAGE_W), (cntr2 + self.config.IMAGE_H)))
            else:
                return i.crop((0, 0, self.config.IMAGE_W, self.config.IMAGE_H))

    def roll(self, i):
        if self.config.ROTATE in range(1, 360):
            if self.config.ROTATE_REVERSE is True:
                return i.rotate(360 - self.config.ROTATE)
            else:
                return i.rotate(self.config.ROTATE)

    def black_n_white(self, i):
        if self.config.WHITE_BLACK is True:
            return i.convert(mode='L')

    def run(self):
        for x in os.listdir('media/'):
            print(f'Editing {x}')
            i = Image.open(f'media/{x}')
            i = self.cut(i)
            i = self.roll(i)
            i = self.black_n_white(i)
            i.save(f'media/{x}')
