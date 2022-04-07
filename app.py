from PIL import Image
from PIL.ImageColor import getcolor

white = getcolor('white', 'RGB')
black = getcolor('black', 'RGB')
red   = getcolor('red', 'RGB')

@profile
def line(x0: int, y0: int, x1: int, y1: int, image: Image.Image, color: tuple) -> None:
    steep = False
    if abs(x1 - x0) < abs(y1 - y0):
        steep = True
        x0, x1, y0, y1 = y0, y1, x0, x1
    if x0 > x1:
        x0, x1, y0, y1 = x1, x0, y1, y0

    dx = x1 - x0
    dy = y1 - y0
    for x in range(x0, x1 + 1):
        t = (x - x0) / dx
        y = int(y0 + t * dy)
        # if steep:
        #     image.putpixel((y, x), color)
        # else:
        #     image.putpixel((x, y), color)

def main():
    image = Image.new('RGB', (100, 100), black)
    
    for _ in range(3000):
        # line(13, 20, 80, 40, image, white)
    # line(20, 13, 40, 80, image, red)
        line(80, 40, 13, 20, image, red)

    # image = image.transpose(1) # Flip vertical
    # image.show()

if __name__ == "__main__":
    main()
