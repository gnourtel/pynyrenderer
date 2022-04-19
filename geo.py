
from __future__ import annotations
from typing import Union

class Vertex():
    x: float
    y: float
    z: float

    def __init__(self, vertex: Union[list[float], str] = None) -> None:
        if type(vertex) == list:
            self.x, self.y, self.z = vertex
        elif type(vertex) == str:
            self.x, self.y, self.z = map(lambda x: float(x), vertex.strip()[2:].split())
        else:
            raise UserWarning(f"unsupport vertex input type {type(vertex)}")

    def __eq__(self, vertex: Vertex) -> bool:
        return self.x == vertex.x and self.y == vertex.y

    def __xor__(self, v: Vertex) -> Vertex:
        return self.__class__([
            self.y * v.z - self.z * v.y,
            self.z * v.x - self.x * v.z,
            self.x * v.y - self.y * v.x
        ])