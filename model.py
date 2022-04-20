from typing import Generator
from geo import Vector

class Model():
    def __init__(self, model_url: str) -> None:
        with open(model_url, "r") as rd:
            self.model = rd.readlines()

    def get_vertex(self) -> Generator[list[Vector], None, None]:
        for line in self.model:
            if line[0] == "f":
                vertices  = [ vertex.split("/")[0] for vertex in line.strip()[2:].split(" ") ]
                yield [ Vector(self.model[int(v) - 1]) for v in vertices ]
