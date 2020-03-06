import os
from io import BytesIO
from random import randint

from PIL import Image, ImageDraw, ImageFont


class VerifyCode:
    def __init__(self, width=100, height=40, size=4):
        self.width = width
        self.height = height
        self.size = size
        self.__code = ''
        self.pen = None

    @property
    def code(self):
        return self.__code

    def generate(self):
        im=Image.new('RGB',(self.width,self.height),self.__rand_color(120))
        # im = Image.new('RGB', (self.width, self.height), self.__rand_color(120))
        self.pen = ImageDraw.Draw(im)
        self.rander_string()
        self.__draw_code()
        self.__draw_point()
        self.__draw_line()
        buf = BytesIO()
        im.save(buf, 'png')
        res = buf.getvalue()
        buf.close()
        return res

    def rander_string(self):
        self.__code = ''
        for i in range(self.size):
            self.__code += str(randint(0, 9))
        print(self.__code)

    def __rand_color(self, min=0, max=255):
        return randint(min, max), randint(min, max), randint(min, max)

    def __draw_code(self):
        path = os.path.join(os.getcwd(), 'static/fonts/SIMLI.TTF')
        print(path)
        font1 = ImageFont.truetype(path, size=37, encoding='utf-8')
        width = (self.width - 20) // self.size
        for i in range(len(self.__code)):
            x = 12 + width * i
            self.pen.text((x, 9), self.__code[i], font=font1, fill=self.__rand_color(0,0))

    def __draw_point(self):
        for i in range(100):
            self.pen.point((randint(1, self.width - 1), randint(1, self.height - 1)), self.__rand_color(30, 100))

    def __draw_line(self):
        for i in range(5):
            self.pen.line([(randint(1, self.width - 1), randint(1, self.height - 1)),
                           (randint(1, self.width - 1), randint(1, self.height - 1))], fill=self.__rand_color(50,150),
                          width=5)

vc=VerifyCode()

if __name__ == '__main__':
    pass
