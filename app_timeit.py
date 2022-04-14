import timeit
from app import line, NPImage, np, getcolor


def test_line():
    # declare color
    white = np.asarray(getcolor('white', 'RGB'), dtype=np.uint8)
    black = np.asarray(getcolor('black', 'RGB'), dtype=np.uint8)
    red   = np.asarray(getcolor('red', 'RGB'), dtype=np.uint8)

    # init np array image
    np_image = NPImage(100, 100, black)
    
    # init timer
    number = 30000
    t = timeit.Timer(lambda: line(13, 20, 80, 40, np_image, white), 'gc.enable()')
    timing = t.timeit(number=number)
    print(f"{number} loops, total: {timing:.5f} sec, avg: {timing / number:.3g} sec")

if __name__ == "__main__":
    test_line()
