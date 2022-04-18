from typing import Union, Generator

class Vertex():
    _x: float
    _y: float
    _z: float
    width: int
    height: int
    def __init__(self, vertex: Union[list[float], str] = None) -> None:
        if type(vertex) == list:
            self._x, self._y, self._z = vertex
        elif type(vertex) == str:
            self._x, self._y, self._z = map(lambda x: float(x), vertex.strip()[2:].split())
        else:
            raise UserWarning(f"unsupport vertex input type {type(vertex)}")


class Model():
    def __init__(self, model_url: str) -> None:
        with open(model_url, "r") as rd:
            self.model = rd.readlines()

    def get_vertex(self) -> Generator[list[Vertex], None, None]:
        for line in self.model:
            if line[0] == "f":
                vertices  = [ vertex.split("/")[0] for vertex in line.strip()[2:].split(" ") ]
                yield [ Vertex(self.model[int(v) - 1]) for v in vertices ]
