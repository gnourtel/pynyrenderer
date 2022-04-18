from PIL import Image
from np_image import NPImage, RGBColor
from model import Model, Vertex

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

def triangle(v0: Vertex, v1: Vertex, v2: Vertex, np_image: NPImage, color) -> None:
    # Line sweeping way
    if v0.y > v1.y: v0, v1 = v1, v0
    if v0.y > v2.y: v0, v2 = v2, v0
    if v1.y > v2.y: v1, v2 = v2, v1

    total_length = v2.y - v0.y
    segment_length_1 = v1.y - v0.y
    segment_length_2 = v2.y - v1.y
    for y in range(v0.y, v2.y + 1):
        x_alpha = v0.x + int((v2.x - v0.x) * (y - v0.y) / total_length)
        if y <= v1.y:
            x_beta  = v0.x + int((v1.x - v0.x) * (y - v0.y) / segment_length_1)
        else:
            x_beta  = v1.x + int((v2.x - v1.x) * (y - v1.y) / segment_length_2)
        if x_alpha > x_beta: x_alpha, x_beta = x_beta, x_alpha
        for moving_x in range(x_alpha, x_beta + 1):
            np_image.set_color(moving_x - 1, y - 1, color)


def main():
    # declare color
    white = RGBColor("white")
    black = RGBColor("black")
    red   = RGBColor("red")
    green = RGBColor("green")

    # init np array image
    height = 200
    width = 200
    np_image = NPImage(height, width, black)
    

    # # Chapter 1
    # # read model
    # model = Model("object/head_wireframe.obj")
    #
    # for vertices in model.get_vertex():
    #     for i in range(len(vertices)):
    #         v0 = vertices[i]
    #         v1 = vertices[(i + 1) % 3]
    #         x0 = int((v0.x + 1.) * width / 2.)
    #         y0 = int((v0.y + 1.) * height / 2.)
    #         x1 = int((v1.x + 1.) * width / 2.)
    #         y1 = int((v1.y + 1.) * height / 2.)
    #         line(x0, y0, x1, y1, np_image, white)

    # Chapter 2
    t0 = [ Vertex([10, 70, 0]), Vertex([50, 160, 0]), Vertex([70, 80, 0]) ]
    t1 = [ Vertex([180, 50, 0]), Vertex([150, 1, 0]), Vertex([70, 180, 0]) ]
    t2 = [ Vertex([180, 150, 0]), Vertex([120, 160, 0]), Vertex([130, 180, 0]) ]
    triangle(t0[0], t0[1], t0[2], np_image, red)
    triangle(t1[0], t1[1], t1[2], np_image, white)
    triangle(t2[0], t2[1], t2[2], np_image, green)

    image = Image.fromarray(np_image.data, 'RGB')
    image = image.transpose(2) # Flip vertical
    image.show()

if __name__ == "__main__":
    main()
