from PIL import Image
from np_image import NPImage, RGBColor
from model import Model

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
            np_image.set_color(y - 1, x - 1, color)
        else:
            np_image.set_color(x - 1, y - 1, color)

        error_new += derror_new
        if error_new > dx:
            y += 1 if y1 > y0 else -1
            error_new -= dx * 2

def main():
    # declare color
    white = RGBColor("white")
    black = RGBColor("black")

    # init np array image
    height = 800
    width = 800
    np_image = NPImage(height, width, black)
    
    # read model
    model = Model("object/head_wireframe.obj")

    # Chapter 1
    for vertices in model.get_vertex():
        for i in range(len(vertices)):
            v0 = vertices[i]
            v1 = vertices[(i + 1) % 3]
            x0 = int((v0.x + 1.) * width / 2.)
            y0 = int((v0.y + 1.) * height / 2.)
            x1 = int((v1.x + 1.) * width / 2.)
            y1 = int((v1.y + 1.) * height / 2.)
            line(x0, y0, x1, y1, np_image, white)

    image = Image.fromarray(np_image.data, 'RGB')
    image = image.transpose(2) # Flip vertical
    image.show()

if __name__ == "__main__":
    main()
