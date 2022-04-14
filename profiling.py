from app import line, NPImage, np, getcolor
import cProfile

def test_line():
    # declare color
    white = np.asarray(getcolor('white', 'RGB'), dtype=np.uint8)
    black = np.asarray(getcolor('black', 'RGB'), dtype=np.uint8)
    red   = np.asarray(getcolor('red', 'RGB'), dtype=np.uint8)

    # init np array image
    np_image = NPImage(100, 100, black)
    
    # init timer
    with cProfile.Profile() as pr:
        for _ in range(30000):
            line(13, 20, 80, 40, np_image, white)
    pr.print_stats()

if __name__ == "__main__":
    test_line()
