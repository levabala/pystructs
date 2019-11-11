from dataclasses import dataclass
from vector import Vector
from point import Point


@dataclass
class Line:
  p: Point
  v: Vector
