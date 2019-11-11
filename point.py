from dataclasses import dataclass
from vector import Vector


@dataclass
class Point:
  x: float
  y: float

  def __add__(self, p2):
    return Point(self.x + p2.x, self.y + p2.y)

  def __sub__(self, p2) -> Vector:
    return Vector(p2.x - self.x, p2.y - self.y)

  def __str__(self):
    return "{}:{}".format(self.x, self.y)
