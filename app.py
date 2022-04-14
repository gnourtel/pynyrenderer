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

class Model():
    def __init__(self, model: list[str]) -> None:
        self.model = model
    
    def get_vertex(self):
        for line in self.model:
            if line[0] == "f":
                vertices  = [vertex.split("/")[0] for vertex in line.strip()[2:].split(" ")]
                yield [ self.model[int(v) - 1].strip()[2:].split(" ") for v in vertices ]

def line(x0: int, y0: int, x1: int, y1: int, np_image: NPImage, color) -> None:
    steep = False
    if abs(x1 - x0) < abs(y1 - y0):
        steep = True
        x0, x1, y0, y1 = y0, y1, x0, x1
    if x0 > x1:
        x0, x1, y0, y1 = x1, x0, y1, y0

    dx = x1 - x0
    dy = y1 - y0

    # 4th attemp
    # derror = abs(dy/dx)
    # error = 0.0
    # y = y0
    # for x in range(x0, x1 + 1):
    #     if steep:
    #         np_image.set_color(y, x, color)
    #     else:
    #         np_image.set_color(x, y, color)
    #     error += derror
    #     if error > 0.5:
    #         y += 1 if y1 > y0 else -1
    #         error -= 1

    # 5th attempt
    derror_new = abs(dy) * 2
    error_new = 0 
    y = y0
    for x in range(x0, x1 + 1):
        if steep:
            np_image.set_color(y, x, color)
        else:
            np_image.set_color(x, y, color)

        error_new += derror_new
        if error_new > dx:
            y += 1 if y1 > y0 else -1
            error_new -= dx * 2

def main():
    # declare color
    white = np.asarray(getcolor('white', 'RGB'), dtype=np.uint8)
    black = np.asarray(getcolor('black', 'RGB'), dtype=np.uint8)

    # init np array image
    height = 800
    width = 800
    np_image = NPImage(height, width, black)
    
    # read model
    with open("object/head_wireframe.obj", "r") as rd:
        model = Model(rd.readlines())

    for v in model.get_vertex():
        for e in range(3):
            v0 = v[e]
            v1 = v[(e + 1) % 3]
            x0 = int((float(v0[0]) + 1.) * width / 2.) - 1
            y0 = int((float(v0[1]) + 1.) * height / 2.) - 1
            x1 = int((float(v1[0]) + 1.) * width / 2.) - 1
            y1 = int((float(v1[1]) + 1.) * height / 2.) - 1
            line(x0, y0, x1, y1, np_image, white)

    image = Image.fromarray(np_image.data, 'RGB')
    image = image.transpose(2) # Flip vertical
    image.show()

if __name__ == "__main__":
    main()
