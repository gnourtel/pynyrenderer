import numpy as np
from dataclasses import dataclass


class RGBColor():
    color_palette = {
        "red": np.array([255, 0, 0], dtype=np.uint8),
        "green": np.array([0, 255, 0], dtype=np.uint8),
        "blue": np.array([0, 0, 255], dtype=np.uint8),
        "black": np.array([0, 0, 0], dtype=np.uint8),
        "white": np.array([255, 255, 255], dtype=np.uint8),
    }
    def __init__(self, color_str: str) -> None:
        self.value = self.color_palette.get(color_str)
        if self.value is None:
            raise UserWarning(f"Unsupport color value: {color_str}")

class NPImage():
    def __init__(self, h, w, bg = None) -> None:
        if bg is None:
            self.data = np.full((h, w, 3), dtype=np.uint8, fill_value=bg)
        else:
            self.data = np.zeros((h, w, 3), dtype=np.uint8)

    def set_color(self, x, y, color: RGBColor):
        self.data[x, y] = color.value