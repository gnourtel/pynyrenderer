import numpy as np
from PIL import Image
from PIL.ImageColor import getcolor

class NPImage():
    def __init__(self, h, w, bg = None) -> None:
        if bg is None:
            self.data = np.full((h, w, 3), dtype=np.uint8, fill_value=bg)
        else:
            self.data = np.zeros((h, w, 3), dtype=np.uint8)

    def set_color(self, x, y, color):
        self.data[x, y] = color


def line(x0: int, y0: int, x1: int, y1: int, np_image: NPImage, color) -> None:
    steep = False
    if abs(x1 - x0) < abs(y1 - y0):
        steep = True
        x0, x1, y0, y1 = y0, y1, x0, x1
    if x0 > x1:
        x0, x1, y0, y1 = x1, x0, y1, y0

    dx = x1 - x0
    dy = y1 - y0
    derror = abs(dy/dx)
    error = 0.0
    y = y0
    for x in range(x0, x1 + 1):
        if steep:
            np_image.set_color(y, x, color)
        else:
            np_image.set_color(x, y, color)

        error += derror
        if error > 0.5:
            y += 1 if y1 > y0 else -1
            error -= 1

def main():
    # declare color
    white = np.asarray(getcolor('white', 'RGB'), dtype=np.uint8)
    black = np.asarray(getcolor('black', 'RGB'), dtype=np.uint8)
    red   = np.asarray(getcolor('red', 'RGB'), dtype=np.uint8)

    # init np array image
    np_image = NPImage(100, 100, black)
    
    line(13, 20, 80, 40, np_image, white)
    line(20, 13, 40, 80, np_image, red)
    line(80, 40, 13, 20, np_image, red)

    image = Image.fromarray(np_image.data, 'RGB')
    image = image.transpose(1) # Flip vertical
    image.show()

if __name__ == "__main__":
    main()
