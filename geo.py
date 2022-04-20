
from __future__ import annotations
from typing import Union
import numpy as np

class Vector():
    def __init__(self, vertices: Union[list[float], str, np.ndarray]) -> None:
        if type(vertices) == list:
            self.data = np.array(vertices)
        elif type(vertices) == str:
            self.data = np.array(list(
                map(lambda x: float(x), vertices.strip()[2:].split())))
        elif type(vertices) == np.ndarray:
            self.data: np.ndarray = vertices
        else:
            raise UserWarning(f"unsupport vertex input type {type(vertices)}")
        self.x = self.data[0]
        self.y = self.data[1]
        self.z = self.data[2] if self.data.shape[0] >= 3 else 0.

    def __str__(self):
        return f"Array[{self.x}, {self.y}, {self.z}]"

    def __add__(self, v: Vector) -> Vector:
        return Vector(self.data + v.data)

    def __sub__(self, v: Vector) -> Vector:
        return Vector(self.data - v.data)

    def __mul__(self, v_or_f: Union[Vector, float, int]) -> Union[Vector, float]:
        if type(v_or_f) == Vector:
            return float(np.dot(self.data, v_or_f.data))
        elif type(v_or_f) in {float, int}:
            return Vector(self.data * v_or_f)
        else:
            raise UserWarning(f"unsupport * operator for array and {type(v_or_f)}")

    def __truediv__(self, num: Union[float, int]) -> Vector:
        return Vector(self.data / num)

    def __xor__(self, v: Vector) -> Vector:
        return Vector(np.cross(self.data, v.data))

    def nomalize(self) -> Vector:
        return Vector(self.data / np.linalg.norm(self.data))
