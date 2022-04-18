import cProfile
from sys import argv
from app import line, triangle
from model import Vertex
from np_image import NPImage, RGBColor

def test_line(number):
    # declare color
    white = RGBColor("white")
    black = RGBColor("black")

    # init np array image
    np_image = NPImage(100, 100, black)
    
    # init timer
    with cProfile.Profile() as pr:
        for _ in range(number):
            line(13, 20, 80, 40, np_image, white)
    pr.print_stats()

def test_triangle(number):
    # declare color
    white = RGBColor("white")
    black = RGBColor("black")

    # init np array image
    np_image = NPImage(200, 200, black)
    t0 = [ Vertex([10, 70, 0]), Vertex([50, 160, 0]), Vertex([70, 80, 0]) ]
    # t1 = [ Vertex([180, 50, 0]), Vertex([150, 1, 0]), Vertex([70, 180, 0]) ]
    # t2 = [ Vertex([180, 150, 0]), Vertex([120, 160, 0]), Vertex([130, 180, 0]) ]

    # init timer
    with cProfile.Profile() as pr:
        for _ in range(number):
            triangle(t0[0], t0[1], t0[2], np_image, white)
            # triangle(t1[0], t1[1], t1[2], np_image, white)
            # triangle(t2[0], t2[1], t2[2], np_image, white)
            
    pr.print_stats()


if __name__ == "__main__":
    if argv[1] == "line":
        number = 30000
        test_line(number=number)
    elif argv[1] == "triangle":
        number = 1000
        test_triangle(number=number)
