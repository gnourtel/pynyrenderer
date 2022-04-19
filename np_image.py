import numpy as np


class RGBColor():
    color_palette = {
        "red": np.array([255, 0, 0], dtype=np.uint8),
        "green": np.array([0, 255, 0], dtype=np.uint8),
        "blue": np.array([0, 0, 255], dtype=np.uint8),
        "black": np.array([0, 0, 0], dtype=np.uint8),
        "white": np.array([255, 255, 255], dtype=np.uint8),
    }

    def __init__(self, color_str: str = None) -> None:
        if color_str:
            self.value = self.color_palette.get(color_str)
        else:
            self.value = np.random.randint(255, size=3)

    @classmethod
    def random_color(cls):
        return cls()


class NPImage():
    def __init__(self, h, w, bg = None) -> None:
        self.h = h
        self.w = w
        if bg is None:
            self.data = np.full((h, w, 3), dtype=np.uint8, fill_value=bg)
        else:
            self.data = np.zeros((h, w, 3), dtype=np.uint8)

    def set_color(self, x, y, color: RGBColor):
        self.data[x, y] = color.value
